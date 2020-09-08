# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # Lists to store the paths
        arr = []
        ans = 0
        def preorder(root, path,arr):
            # Base Condition
            if root is None:
                return
            # Appending the value to the current path
            path += str(root.val)
            
            # Only append the path to the array if we encounter a Leaf Node
            if root.left is None and root.right is None:
                arr.append(path)
            # Recurring for the left Child
            preorder(root.left, path, arr)
            # Recurring for the right Child
            preorder(root.right, path, arr)
        
        # Calling Preorder function
        preorder(root, '', arr)
        
        # Converting to decimal and adding 
        for i in arr:
            ans += int(i,2)
        
        return ans
        
        
