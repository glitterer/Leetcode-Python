# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None: # baseline
            return 0
        
        #unable to understand (this code is actually from the other answers)
        if root.left:
            if root.left.left is None and root.left.right is None:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else: # no leaf
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        else: # no left (right만 있는 것 x)
            return self.sumOfLeftLeaves(root.right)