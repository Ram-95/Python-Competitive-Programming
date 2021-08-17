# O(N) Time and Space - Storing the Good Nodes and count them at last.
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

# O(N) Time and O(H) Space. - No list used
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, ans: list, maxm: float) -> int:
            if root is None:
                return 0          
            maxm = max(root.val, maxm)
            return int(root.val >= maxm) + dfs(root.left, ans, maxm) + dfs(root.right, ans, maxm)
        
        ans = 0
        return dfs(root, ans, root.val)
