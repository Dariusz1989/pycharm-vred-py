'''
vrRenderLayerModule
------------------------------------------
API version: v1 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------

'''

from typing import List


def activateRenderLayer(name):
    '''
    Activates a renderlayer.
    '''
    pass


def activateRenderLayerState(name):
    '''
    Activates stored node visibility states for the whole scene.
    '''
    pass


def addNodesToRenderLayer(nodes, layerName):
    '''
    Add nodes to a renderlayer.
    '''
    pass


def createRenderLayer(name):
    '''
    Activates a renderlayer.
    '''
    pass


def resetNodeVisibilityFlags(node):
    '''
    Resets the node visibility flags for a given node and its children.
    '''
    pass


def resetRenderLayers():
    '''
    Resets all activated render layers.
    '''
    pass


def setNodeVisibilityFlags(visible, node, receiveShadows, overrideMaterial, visibleInRefractions, doubleSided, primaryVisibility, visibleInReflections, visibleForPhotons, castShadowOnShadowMaterial, castShadows, useOverrideMaterial, visibleInAlpha):
    '''
    Sets the visibility flags and the override material for a given node and its children.
    '''
    pass

