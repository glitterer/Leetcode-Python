# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        sums = []

        def dfs(node, depth):
            if node is None:
                return
            if len(sums) == depth:
                sums.append(node.val)
            else:
                sums[depth] += node.val
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root, 0)
        
        print(sums)
        return sums[-1]
