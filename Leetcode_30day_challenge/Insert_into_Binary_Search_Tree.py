""" Time: O(N) and Space: O(1) """
# Iterative Solution
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
        else:
            t_root = root
            while True:
                if t_root.val < val:
                    if t_root.right:
                        t_root = t_root.right
                    else:
                        t_root.right = TreeNode(val)
                        break
                else:
                    if t_root.left:
                        t_root = t_root.left
                    else:
                        t_root.left = TreeNode(val)
                        break

        return root
            

# Recursive Solution
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
