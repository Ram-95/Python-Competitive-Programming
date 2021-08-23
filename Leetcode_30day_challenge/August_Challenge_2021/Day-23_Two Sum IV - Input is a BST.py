# TC: O(N) | SC: O(N)
# Method - 1: Traverse the BST, store the nodes values in a Dictionary. Then find the sum of two numbers equals target.
from collections import defaultdict
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d = defaultdict(int)
        if root.left is None and root.right is None:
            return False
        def inorder(root, d):
            if root is None:
                return
            inorder(root.left, d)
            d[root.val] += 1
            inorder(root.right, d)
        
        inorder(root, d)
        
        for i in d.keys():
            val = k - i
            if val in d and val != i:
                return True
        
        return False
        
# Method - 2: Since it is a BST, for every element we can search for the element b (b = target - node.val) in O(H) Time. 
# TC: O(N) and space will now be O(H) [Best: logN and Worst: N]
