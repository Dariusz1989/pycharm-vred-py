'''
vrdPerspectiveMatch
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Class to access camera perspective matching functionality.
'''

from typing import List


class QVector3D():
    pass


class VanishingLinesType():
    pass


def doRotateLeft():
    '''
    Rotates the camera clockwise around the pivot by the amount of degrees set with         vrdPerspectiveMatch.setRotationStepSize(deg)
    '''
    pass


def doRotateRight():
    '''
    Rotates the camera counterclockwise around the pivot by the amount of degrees set with         vrdPerspectiveMatch.setRotationStepSize(deg)
    '''
    pass


def getEnabled() -> bool:
    '''
    Returns if perspective matching tool is currently enabled.
    '''
    return None


def getMagnifyFactor() -> float:
    '''
    Returns the scale factor used for the magnifier.
    '''
    return None


def getPivot() -> QVector3D:
    '''
    Returns the pivot used for rotations with         vrdPerspectiveMatch.doRotateLeft() and vrdPerspectiveMatch.doRotateRight()
    '''
    return None


def getRotationStepSize() -> float:
    '''
    Returns the rotation step size used by         vrdPerspectiveMatch.doRotateLeft() and vrdPerspectiveMatch.doRotateRight()
    '''
    return None


def getVanishingLinesType() -> VanishingLinesType:
    '''
    Returns the vanishing lines type.
    '''
    return None


def setDefaultLines():
    '''
    Resets the vanishing lines to default values.
    '''
    pass


def setEnabled(enabled: bool):
    '''
    Enables or disables the perspective match tool.
    '''
    pass


def setMagnifyFactor(factor: float):
    '''
    Sets the magnify factor used for the magnifier shown at the manipulator handles. This does not have an effect on the calculation.
    '''
    pass


def setPivot(pivot: QVector3D):
    '''
    Sets the pivot used for rotations with         vrdPerspectiveMatch.doRotateLeft() and vrdPerspectiveMatch.doRotateRight()
    '''
    pass


def setPivotFromNavigator():
    '''
    Applies the currently used navigation pivot as perspective match pivot.
    '''
    pass


def setRotationStepSize(deg: float):
    '''
    Sets the rotation step size used by         vrdPerspectiveMatch.doRotateLeft() and vrdPerspectiveMatch.doRotateRight()
    '''
    pass


def setVanishingLinesType(type: VanishingLinesType):
    '''
    Sets the vanishing lines type defining which vanishing lines should be used (and shown) for perspective matching.
    '''
    pass

