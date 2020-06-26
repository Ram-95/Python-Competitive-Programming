# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def solve(root, prev):
            if root is None:
                return 0
            n = len(str(root.val))
            curr = prev * (10**n) + root.val
            if root.left is None and root.right is None:
                return curr
            return solve(root.left,curr) + solve(root.right, curr)
        
        return solve(root, 0)
        
        
