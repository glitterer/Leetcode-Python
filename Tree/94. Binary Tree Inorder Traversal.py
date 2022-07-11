# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        if root is not None:
            visited.extend(self.inorderTraversal(root.left))
            visited.append(root.val)
            visited.extend(self.inorderTraversal(root.right))
        return visited
