# O(N) Time and Space.
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, ans: list, maxm: float) -> int:
            if root is None:
                return           
            maxm = max(root.val, maxm)
            if root.val >= maxm:
                ans.append(root.val)
            
            dfs(root.left, ans, maxm)
            dfs(root.right, ans, maxm)
        
        ans = []
        dfs(root, ans, float('-inf'))
        return len(ans)
