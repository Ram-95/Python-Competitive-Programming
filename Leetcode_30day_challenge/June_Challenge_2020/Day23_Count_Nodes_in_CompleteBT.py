# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        global ans
        ans = 0
        def inorder(root):
            global ans
            if root is None:
                return
            
            inorder(root.left)
            ans += 1
            inorder(root.right)
        
        inorder(root)
        return ans
