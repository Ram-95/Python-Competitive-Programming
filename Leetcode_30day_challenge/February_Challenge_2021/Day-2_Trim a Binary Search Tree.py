'''My Solution - O(N) Time and Space.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None
        
        # If the current nodes value is less than low, then trim the right subtree
        if low > root.val:
            return self.trimBST(root.right, low, high)
        
        # If the current nodes value is greater than high, then trim the left subtree
        elif high < root.val:
            return self.trimBST(root.left, low, high)
        
        # If none of the above conditions are met, then trim the left and right subtrees
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        
        return root
        
