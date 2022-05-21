# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sums = 0
        def helper(root, sums): # helper 만들기
            if root is None:
                return 0
            else:
                sums = sums*2 + root.val # from Tutor
                if root.left is None and root.right is None:
                    return sums
                else:
                    return helper(root.left, sums) + helper(root.right, sums)
        return helper(root, sums)
    '''
    
    
    
    def sumRootToLeaf(self, root: Optional[TreeNode], sums = 0) -> int:
        if root is None:
            return 0
        else:
            sums = sums*2 + root.val # from Tutor
            if root.left is None and root.right is None:
                return sums
            else:
                return self.sumRootToLeaf(root.left, sums) + self.sumRootToLeaf(root.right, sums)
