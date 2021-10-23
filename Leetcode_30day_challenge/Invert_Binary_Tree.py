# Given the root of a binary tree, invert the tree, and return its root.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(root):
            if root is None:
                return
            # Swapping the left and right nodes
            root.left, root.right = root.right, root.left
            
            # Recur on both sides
            solve(root.left)
            solve(root.right)
        
        solve(root)
        return root
