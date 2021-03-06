'''
vrdAimConstraintNode
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
This class gives access to an aim constraint object in VRED. An aim constraint will compute the orientation of a constrained object depending on the position of a target and an optional up vector target. If there are multiple targets or up vector targets, the positions are calculated as the weighted average value of it.
'''

from typing import List


class vrdNode():
    pass


def clearUpVectorTargetNodes():
    '''
    Clears the set up vector target nodes of the constraint.
    '''
    pass


def getUpVectorTargetNodes() -> List[vrdNode]:
    '''
    Returns the list of nodes set as up vector targets for the constraint.
    '''
    return None


def getUpVectorTargetNodeWeight(node: vrdNode) -> float:
    '''
    Gets the weight for a up vector target node of the constraint. The node must be referenced in the up vector target nodes list of the constraint.
    '''
    return None


def setUpVectorTargetNodes(nodes: List[vrdNode]):
    '''
    Sets a list of nodes as up vector targets for the constraint.
    '''
    pass


def setUpVectorTargetNodeWeight(node: vrdNode, weight: float):
    '''
    Sets the weight for an up vector target node of the constraint. The node must be referenced in the up vector target nodes list of the constraint.
    '''
    pass

