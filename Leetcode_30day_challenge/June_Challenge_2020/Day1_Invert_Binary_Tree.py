'''
Given a Binary Tree, return it's Mirror Image.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right= right
class Solution:
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        #Swapping the Left and Right Nodes.
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        
