#### Traversing Right-Root-Left and updating the Root values | O(N) Time & Space
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        global sums
        sums = 0
        traverse(root)
        return root

# Right-Root-Left Traversal of BST. Updates the root values during traversal itself.
def traverse(root):
    global sums
    if root is None:
        return
	# Recurring on the Right side
    traverse(root.right)
    sums += root.val
    root.val = sums
	# Recurring on the Left side
    traverse(root.left)
        
```
