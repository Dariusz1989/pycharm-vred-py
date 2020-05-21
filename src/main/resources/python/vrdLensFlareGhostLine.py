'''
vrdLensFlareGhostLine
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
This class is used for collection ghost effects. Objects of this class acts as a container for     vrdLensFlareGhost objects. But it is an effect too. This class has a name and if becomes inactive, all ghosts of this line becomes inactive.
'''

from typing import List


class vrdLensFlareGhost():
    pass


def createGhost(distance: float) -> vrdLensFlareGhost:
    '''
    A new ghost will be created for this line. The new ghost object has default properties. A �ghost� property signal is emitted for the line object.
    '''
    return None


def getGhosts() -> List[vrdLensFlareGhost]:
    '''
    Get a list of all ghost of this line.
    '''
    return None


def removeGhosts(ghosts: List[vrdLensFlareGhost]):
    '''
    Remove some ghosts of this line. It will be checked, if the given ghosts are in this line. A �ghost� property signal is emitted for the line object. But this only happens when ghosts have been removed. If the parameter list was empty, the signal is not sent. If the ghosts were not in this line, the signal will not be sent either.
    '''
    pass

