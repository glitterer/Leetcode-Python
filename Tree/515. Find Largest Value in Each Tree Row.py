# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        mapping = {}
        def helper(node, depth):
            if node is None:
                return
            if depth not in mapping.keys():
                mapping[depth] = node.val
            else:
                mapping[depth] = max(node.val, mapping[depth])
            
            helper(node.right, depth+1)
            helper(node.left, depth+1)
        
        helper(root, 0)
        
        res = []
        for k,v in mapping.items():
            res.append(v)
        
        return res
