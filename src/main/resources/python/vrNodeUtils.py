'''
vrNodeUtils
------------------------------------------
API version: v1 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------

'''

from typing import List


def addFaceNormals(root_node):
    '''
    See calcFaceNormals with the exception that the calculation is only performed for geometries without normals.
    '''
    pass


def cacheVBO(node):
    '''
    Deprecated and not functional anymore! Rebuilds all vertex buffer objects for the whole scene or the given subtree node.
    '''
    pass


def calcFaceNormalRepresentation(length):
    '''
    Creates visualization geometry for face normals.
    '''
    pass


def calcFaceNormals(root_node):
    '''
    Calculates new vertex normals based on face normals.
    '''
    pass


def calcNormalAndBitangent(binormalTarget, tangentTarget, root_node, textureUnit):
    '''
    Calculates tangents and binormals depending on vertex normals and texture coordinates.
    '''
    pass


def calcSecondaryColorRepresentation(length):
    '''
    Creates visualization geometry for secondary vertex colors.
    '''
    pass


def calcVertexColorRepresentation(length):
    '''
    Creates visualization geometry for vertex colors.
    '''
    pass


def calcVertexNormalRepresentation(length):
    '''
    Creates visualization geometry for vertex normals.
    '''
    pass


def calcVertexNormals(angle, root_node):
    '''
    Calculates new and smooth vertex normals.
    '''
    pass


def convertAllToComponentTransform(root_node):
    '''
    Converts all Transform nodes of a given subgraph to VRML-ComponentTransform nodes.
    '''
    pass


def convertAllToTransform(root_node):
    '''
    Converts all Component transform nodes of a given subgraph to normal transform nodes.
    '''
    pass


def createAttachment(type):
    '''
    Creates a new attachment of a given type
    '''
    pass


def createBox(red, blue, size_x, res_x, res_y, size_y, size_z, green, res_z, alpha):
    '''
    Creates a box object of size x/y/z in a given rgb color.
    '''
    pass


def createCone(radius, red, height, blue, create_side, create_bottom, green, sides):
    '''
    Creates a cone, or parts of it, in a given size and color.
    '''
    pass


def createCylinder(radius, red, height, blue, create_side, create_bottom, green, sides, create_top):
    '''
    Creates a cylinder, or parts of it, in a given size and color.
    '''
    pass


def createEnvBox(red, blue, res_x, res_y, green, res_z, size, texture, transparency):
    '''
    Creates a box with an environment texture.
    '''
    pass


def createLatLongSphere(red, radius, latres, longres, blue, green):
    '''
    Creates a sphere in a given size and color, with two different resolutions.
    '''
    pass


def createLine(red, ax, blue, green, ay, bx, bz, az, by):
    '''
    Creates a line from point a to point b in a given rgb color.
    '''
    pass


def createMipmaps():
    '''
    Creates mipmaps for all textures.
    '''
    pass


def createPlane(red, blue, size_x, res_x, res_y, size_y, green):
    '''
    Creates a plane object of size x/y in a given rgb color.
    '''
    pass


def createShellNodes(node):
    '''
    Converts groups to shell nodes if all children are surfaces.
    '''
    pass


def createSphere(red, radius, blue, green, resolution):
    '''
    Creates a sphere in a give size and color.
    '''
    pass


def degToRad(degrees):
    '''
    Converts degrees to radians.
    '''
    pass


def downscaleTextures(factor):
    '''
    Downscale all textures within the scene.
    '''
    pass


def findLargestGeometry(max_tris_limit):
    '''
    Returns the largest geometry with the number of triangles smaller than max_tris_limit.
    '''
    pass


def getBoundingBoxCenter(worldSpace, node):
    '''
    Gets the center of the object bounding volume.
    '''
    pass


def getMirroredNodes(root_node, invert):
    '''
    Returns all mirrored geometry nodes.
    '''
    pass


def getTransformNodeEulerRotationOrder(node):
    '''
    Gets the rotation order of a transform node.
    '''
    pass


def getTransformNodeRotatePivot(worldSpace, node):
    '''
    Gets the rotate pivot of a transform node.
    '''
    pass


def getTransformNodeRotatePivotTranslation(node):
    '''
    Gets the rotate pivot translation value of a transform node (This translation has been introduced to prevent an object from moving when the pivot is moved).
    '''
    pass


def getTransformNodeRotation(node):
    '''
    Gets the rotation value of a transform node.
    '''
    pass


def getTransformNodeRotationOrientation(node):
    '''
    Gets the rotation orientation value of a transform node.
    '''
    pass


def getTransformNodeScale(node):
    '''
    Gets the scale value of a transform node.
    '''
    pass


def getTransformNodeScalePivot(worldSpace, node):
    '''
    Gets the scale pivot of a transform node.
    '''
    pass


def getTransformNodeScalePivotTranslation(node):
    '''
    Gets the scale pivot translation value of a transform node (This translation has been introduced to prevent an object from moving when the pivot is moved)
    '''
    pass


def getTransformNodeShear(node):
    '''
    Gets the shear value of a transform node.
    '''
    pass


def getTransformNodeTranslation(worldSpace, node):
    '''
    Gets the translation value of a transform node.
    '''
    pass


def isBSide(node):
    '''
    Queries the B-Side flag of a node.
    '''
    pass


def normalizeNormals(root_node):
    '''
    Recalculates the vertex normals to have unit length.
    '''
    pass


def normalizeSurfaces(root_node):
    '''
    Normalizes the knot vector of a surfaces.
    '''
    pass


def offsetAlongNormal(offset, root_node):
    '''
    Offsets the geometries vertices along the vertex normal.
    '''
    pass


def optimizeShellSurfaces(node):
    '''
    Reduces memory consumption of Shell Surfaces by removing their names and optimizing some additional data.
    '''
    pass


def optimizeTextures():
    '''
    Optimizes memory usage of textures.
    '''
    pass


def removeUnreferencedNodes(node):
    '''
    Removes unreferenced nodes.
    '''
    pass


def setDisplayList(enable, node):
    '''
    Enables(true)/disables(false) usage of display lists for rendering for the whole scene or a given subgraph.
    '''
    pass


def setGeometryType(nodes, geoTypes):
    '''
    Sets the geometry types for a list of nodes.
    '''
    pass


def setTexturesPriority(priority):
    '''
    Deprecated: Changes the priority of all textures.
    '''
    pass


def setToBSide(isBSide, node):
    '''
    Sets the B-Side flag of a node.
    '''
    pass


def setTransformNodeEulerRotationOrder(node, rotationOrder):
    '''
    Sets the rotation order of a transform node.
    '''
    pass


def setTransformNodeRotatePivot(y, node, z, x, worldSpace):
    '''
    Sets the rotate pivot of a transform node.
    '''
    pass


def setTransformNodeRotatePivotTranslation(y, z, x, node):
    '''
    Sets the rotate pivot translation value of a transform node (This translation has been introduced to prevent an object from moving when the pivot is moved).
    '''
    pass


def setTransformNodeRotation(y, z, x, node):
    '''
    Sets the rotation value of a transform node.
    '''
    pass


def setTransformNodeRotationOrientation(y, z, x, node):
    '''
    Sets the rotation orientation value of a transform node.
    '''
    pass


def setTransformNodeScale(y, z, x, node):
    '''
    Sets the scale value of a transform node.
    '''
    pass


def setTransformNodeScalePivot(y, node, z, x, worldSpace):
    '''
    Sets the scale pn of a transform node.
    '''
    pass


def setTransformNodeScalePivotTranslation(y, z, x, node):
    '''
    Sets the scale pivot translation value of a transform node (This translation has been introduced to prevent an object from moving when the pivot is moved).
    '''
    pass


def setTransformNodeShear(yz, xz, node, xy):
    '''
    Sets the shear value of a transform node.
    '''
    pass


def setTransformNodeTranslation(y, node, z, x, worldSpace):
    '''
    Sets the translation value of a transform node.
    '''
    pass


def setVBO(enable, node):
    '''
    Deprecated: Enables(true)/disables(false) usage of vertex buffer objects for rendering for the whole scene or a given subgraph.
    '''
    pass


def swapFaceNormals(root_node):
    '''
    Swaps the orientation of face normals.
    '''
    pass


def swapNormals(root_node):
    '''
    Swaps the orientation of face and vertex normals.
    '''
    pass


def swapVertexNormals(root_node):
    '''
    Swaps the orientation of vertex normals.
    '''
    pass


def unshareCores(node):
    '''
    Removes core sharing.
    '''
    pass


def updateAmbientOcclusionData(root_node):
    '''
    Fixes ambient occlusion calculations from old vred versions:
    '''
    pass
