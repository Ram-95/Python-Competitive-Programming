# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def insert(root, ele):
            if root is None:
                root = TreeNode(ele)
            elif ele < root.val:
                if root.left is None:
                    root.left = TreeNode(ele)
                else:
                    insert(root.left, ele)
            elif ele > root.val:
                if root.right is None:
                    root.right = TreeNode(ele)
                else:
                    insert(root.right, ele)
                    
        t_root = TreeNode(preorder[0])
        for i in preorder[1:]:
            insert(t_root, i)
        
        return t_root
                    
            
        
