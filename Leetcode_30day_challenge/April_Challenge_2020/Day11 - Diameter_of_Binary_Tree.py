# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, root, ans):
        if root is None:
            return 0
        l_height = self.height(root.left, ans)
        r_height = self.height(root.right, ans)

        ans[0] = max(ans[0], l_height + r_height)
        return 1 + max(l_height, r_height)
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = [-999999999999]
        height_of_tree = self.height(root, ans)
        return ans[0]
