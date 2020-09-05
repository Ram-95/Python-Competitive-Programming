# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # List to store the Inorder traversal elements
        inorder = []
        
        # Inorder Traversal Function
        def inorder_trav(root, inorder):
            if root is None:
                return
            inorder_trav(root.left, inorder)
            inorder.append(root.val)
            inorder_trav(root.right, inorder)
        
        # Inorder traversal of first tree
        inorder_trav(root1, inorder)
        
        # Inorder traversal of second tree
        inorder_trav(root2, inorder)
        
        # Sorting the inorder list
        inorder.sort()
        
        return inorder
            
            
        
