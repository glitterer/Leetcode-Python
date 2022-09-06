# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # source: https://github.com/victiny23/Algorithm_Data_Structure/blob/189d19844f41cc3de54d518bc1c8cd35e914a98c/LC_problems/Depth-First_Search/.ipynb_checkpoints/LC0671%20Second%20Minimum%20Node%20In%20a%20Binary%20Tree-checkpoint.ipynb
        self.min_1 = root.val
        self.min_2 = float(inf)
        
        def dfs(node):
            if node is None:
                return
            if self.min_1 < node.val < self.min_2:
                self.min_2 = node.val
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        
        if self.min_2 < float(inf):
            return self.min_2
        else:
            return -1
