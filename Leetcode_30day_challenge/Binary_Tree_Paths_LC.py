''' https://leetcode.com/problems/binary-tree-paths/submissions/ '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        arr = []
        def preorder(root, path, arr):
            if root is None:
                return
            path += str(root.val) + '->'
            if root.left is None and root.right is None:
                # To avoid the extra '->' at the end
                arr.append(path[:-2])
            preorder(root.left, path, arr)
            preorder(root.right, path, arr)
        
        preorder(root, '', arr)
        return arr
