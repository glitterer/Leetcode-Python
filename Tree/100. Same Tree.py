# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #tree가 없거나
        if p is None and q is None:
            return True
        
        # 하나가 leaf일 때,
        elif p is None or q is None:
            return False
        
        #값들 간의 비교
        elif p.val != q.val:
            return False
        
        #자식간의 재귀 비교
        else: 
            return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
            