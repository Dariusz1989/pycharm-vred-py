package de.chr33z.pycharm.vred;

import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.actionSystem.Presentation;
import com.intellij.openapi.project.Project;
import com.intellij.openapi.projectRoots.Sdk;
import com.intellij.openapi.roots.ProjectRootManager;
import com.intellij.openapi.ui.Messages;
import com.intellij.openapi.vfs.LocalFileSystem;
import com.intellij.openapi.vfs.VirtualFile;
import com.jetbrains.python.sdk.PythonSdkAdditionalData;
import org.jetbrains.annotations.NotNull;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.HashSet;
import java.util.Set;

public class VredAction extends AnAction {

    @Override
    public void actionPerformed(@NotNull AnActionEvent e) {
        Project project = e.getProject();
        if (project == null) {
            Messages.showInfoMessage(
                    "No project detected! Please open or create a python project and try again!\n\nThis plugin is an 'ALPHA' version so please contact the developer if you have any problems: chr33z@gmail.com",
                    "VRED-Py: Error");
            return;
        }

        Sdk sdk = ProjectRootManager.getInstance(project).getProjectSdk();
        if (sdk == null) {
            Messages.showInfoMessage("No project detected! Please open or create a python project and try again!\n\nThis plugin is an 'ALPHA' version so please contact the developer if you have any problems: chr33z@gmail.com", "VRED-Py: Error");
            return;
        }

        try {
            deletePythonDirectories();
        } catch (IOException ioException) {
            ioException.printStackTrace();
        }

        Path pythonApiDirectory = createTempPythonDirectory();
        if (pythonApiDirectory == null) {
            Messages.showInfoMessage("Cannot add vred python api to project. Please contact the creator to figure this out!\n\nThis plugin is an 'ALPHA' version so please contact the developer if you have any problems: chr33z@gmail.com", "VRED-Py: Error");
            return;
        }

        copyPluginResource(pythonApiDirectory);
        setAdditionalPythonPath(sdk, pythonApiDirectory);

        Messages.showInfoMessage(
                "Added VRED Python API to your project path. You can use the autocomplete features after restarting PyCharm.\n\nThis plugin is an 'ALPHA' version so please contact the developer if you have any problems: chr33z@gmail.com",
                "VRED-Py");
    }

    @Override
    public void update(@NotNull final AnActionEvent event) {
        Presentation presentation = event.getPresentation();
        Project project = event.getProject();

        if (project == null) {
            presentation.setEnabled(false);
            return;
        }

        Sdk sdk = ProjectRootManager.getInstance(project).getProjectSdk();
        if (sdk == null) {
            presentation.setEnabled(false);
            return;
        }

        if (!sdk.getName().toLowerCase().contains("python")) {
            presentation.setEnabled(false);
            return;
        }

        presentation.setEnabled(true);
    }

    private void setAdditionalPythonPath(Sdk sdk, Path pythonApiDirectory) {
        PythonSdkAdditionalData additionalData = (PythonSdkAdditionalData) sdk.getSdkAdditionalData();
        if (additionalData != null) {
            VirtualFile pythonPath = LocalFileSystem.getInstance().findFileByPath(pythonApiDirectory.toString());
            Set<VirtualFile> pythonPathSet = new HashSet<VirtualFile>();
            pythonPathSet.add(pythonPath);
            additionalData.setAddedPathsFromVirtualFiles(pythonPathSet);
        }
    }

    private String getPythonDirectoryPrefix() {
        return String.format("pycharm-vred-py_");
    }

    private void deletePythonDirectories() throws IOException {
        File tempDirectory = new File(System.getProperty("java.io.tmpdir"));
        File[] allTempDirectories = getDirectories(tempDirectory);

        String tempDirectoryName = getPythonDirectoryPrefix();
        for (File directory : allTempDirectories) {
            String directoryName = directory.getName();
            if (directoryName.contains(tempDirectoryName)) {
                deleteDirectoryWithFiles(directory.toPath());
            }
        }
    }

    private void deleteDirectoryWithFiles(Path directory) throws IOException {
        Files.walkFileTree(directory, new SimpleFileVisitor<Path>() {
            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                Files.delete(file);
                return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult postVisitDirectory(Path dir, IOException exc) throws IOException {
                Files.delete(dir);
                return FileVisitResult.CONTINUE;
            }
        });
    }

    private Path createTempPythonDirectory() {
        Path pythonApiDirectory = null;
        try {
            String tempDirectoryName = getPythonDirectoryPrefix();
            pythonApiDirectory = Files.createTempDirectory(tempDirectoryName);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return pythonApiDirectory;
    }

    private boolean pythonDirectoryAlreadyExists() {
        File tempDirectory = new File(System.getProperty("java.io.tmpdir"));
        File[] allTempDirectories = getDirectories(tempDirectory);

        boolean pythonDirectoryAlreadyExists = false;

        String tempDirectoryName = getPythonDirectoryPrefix();
        for (File directory : allTempDirectories) {
            String directoryName = directory.getName();
            if (directoryName.startsWith(tempDirectoryName)) {
                pythonDirectoryAlreadyExists = true;
                break;
            }
        }
        return pythonDirectoryAlreadyExists;
    }

    private File[] getDirectories(File directory) {
        return directory.listFiles(File::isDirectory);
    }

    private void copyPluginResource(Path pythonApiDirectory) {
        for (String pythonFileName : PythonFiles.files) {
            try {
                InputStream pythonFileStream = getClass().getResourceAsStream("/python/" + pythonFileName);
                if (pythonFileStream == null) {
                    continue;
                }
                Path destination = pythonApiDirectory.resolve(pythonFileName);
                Files.copy(pythonFileStream, destination);
            } catch (Exception ignored) {
            }
        }
    }
}
