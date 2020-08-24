'''
Find the sum of all left leaves in a given binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        global ans
        ans = 0
        def inorder(root, idx):
            global ans
            if root is None:
                return
            if idx == -1 and (root.left is None and root.right is None):
                #print(f'Matched: {root.val}')
                ans += root.val
            inorder(root.left, -1)
            inorder(root.right, 1)
        
        inorder(root, 0)
        return ans
