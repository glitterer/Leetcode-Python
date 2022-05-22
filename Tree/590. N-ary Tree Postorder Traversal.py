"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        visited = []
        if root is not None:
            for i in range(len(root.children)):
                visited.extend(self.postorder(root.children[i]))
            visited.append(root.val)
        return visited
