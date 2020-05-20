#Solution 1: 
'''Using Inorder Traversal, fill the inorder array and return the k-1th element from the inorder array. 
Time: O(N)
Space: O(N) - For the Inorder Array.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = []
        def inorder_trav(root):
            if root is None:
                return

            inorder_trav(root.left)
            inorder.append(root.val)
            inorder_trav(root.right)
        
        inorder_trav(root)
        
        return inorder[k-1]
        
 #----------------------------------------------------------------------------------------------------------------------------------#
 #Solution - 2
 '''Using Inorder Traversal and storing the answer in a variable and return the answer at the end of the function
 Time: O(N)
 Space: O(1) - NO Array is used.
 '''
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    ans = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root:
            #Recurring on the left child
            self.kthSmallest(root.left, k)
            self.count += 1
            
            #Checking if we found the kth smallest element
            if self.count == k:
                self.ans = root.val
            
            #Recurring on the right child
            self.kthSmallest(root.right, k)
            
        return self.ans
            
