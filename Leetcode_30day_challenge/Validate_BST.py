class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        MIN = float('-inf')
        MAX = float('inf')
        def solve(root, MIN, MAX):
            if root is None:
                return True
            if root.val <= MIN or root.val >= MAX:
                return False
            return solve(root.left, MIN, root.val) and solve(root.right,root.val, MAX)
        return solve(root, MIN, MAX)
