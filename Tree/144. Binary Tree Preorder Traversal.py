# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        if root is not None:
            visited.append(root.val)
            # print(root.val, "afterAppend", visited)
            visited.extend(self.preorderTraversal(root.left))
            # print(root.val, "afterLeft", visited)
            visited.extend(self.preorderTraversal(root.right))
            # print(root.val, "afterRight", visited)
        return visited
        
        
        
        '''
void traversal(node){
    if ( node){
        visit(node); preorder
        traversal(node -> left);
        #visit(node); inorder
        traversal(node -> right);   
        #visit(node); postorder
    }  
}
'''