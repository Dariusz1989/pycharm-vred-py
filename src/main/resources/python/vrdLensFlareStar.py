'''
vrdLensFlareStar
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
This class is used for a sun-like effect, made up of multiple streaks. Use it for things such as street lamps at night, objects with stationary lights, or a light source that�s partially obscured by an object, like a tree or building�s edge. A short introduction can be found under     https://help.autodesk.com/view/VREDPRODUCTS/2020/ENU/?guid=VRED_Lights_About_Lens_Flares_and_Elements_html.
'''

from typing import List


class vrdImage():
    pass


class StarShape():
    pass


def getImage() -> vrdImage:
    '''
    Return the current used texture.
    '''
    return None


def getNumberOfBursts() -> int:
    '''
    Get how many arms a Starburst element has.
    '''
    return None


def getShape() -> StarShape:
    '''
    Get the current used shape.
    '''
    return None


def getThickness() -> float:
    '''
    Get the current used thickness of the effect.
    '''
    return None


def setImage(image: vrdImage):
    '''
    Set an image for this element. You has to change the type to Texture to use the image for the star effect.
    '''
    pass


def setNumberOfBursts(numberOfBursts: int):
    '''
    Use to set how many arms a Starburst element has.
    '''
    pass


def setShape(shape: StarShape):
    '''
    Change its current shape to a fan, spike, blade, or texture.
    '''
    pass


def setThickness(thickness: float):
    '''
    Controls the thickness of the effect.
    '''
    pass

