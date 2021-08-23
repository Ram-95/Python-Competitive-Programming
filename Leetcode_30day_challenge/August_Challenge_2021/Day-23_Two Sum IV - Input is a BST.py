# TC: O(N) | SC: O(N)

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
        
