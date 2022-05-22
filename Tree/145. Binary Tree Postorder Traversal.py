# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        if root is not None:
            visited.extend(self.postorderTraversal(root.left))
            visited.extend(self.postorderTraversal(root.right))
            visited.append(root.val)
        return visited
        
