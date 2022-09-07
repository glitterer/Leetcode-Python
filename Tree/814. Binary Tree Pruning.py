# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        else:
            left = self.pruneTree(root.left)
            right = self.pruneTree(root.right)
            
            if left is None:
                root.left = None
            else:
                root.left = left
            if right is None:
                root.right = None
            else:
                root.right = right
            
            if root.left is None and root.right is None and root.val == 0:
                root = None
            return root
