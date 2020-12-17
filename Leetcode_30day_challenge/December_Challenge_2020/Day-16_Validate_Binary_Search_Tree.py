''' Solution-1 -> O(N) Time and Space '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ans = []
        inorder(root,ans)
        for i in range(len(ans)-1):
            # '=' because duplicates are also allowed
            if ans[i] >= ans[i+1]:
                return False
        return True
    

def inorder(root, ans):
    if root is None:
        return
    inorder(root.left, ans)
    ans.append(root.val)
    inorder(root.right, ans)

#------------------------------------------------------------------------------------------------------------------------------------#

''' Solution-2 -> O(N) Time and O(1) Space'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Class variables
    prev = float('-inf')
    flag = 0
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        
        if self.prev >= root.val:
            self.flag = 1
        self.prev = root.val
        
        self.inorder(root.right)
    
    
    def isValidBST(self, root: TreeNode) -> bool:
        self.inorder(root)
        
        if self.flag == 1:
            return False
        return True
