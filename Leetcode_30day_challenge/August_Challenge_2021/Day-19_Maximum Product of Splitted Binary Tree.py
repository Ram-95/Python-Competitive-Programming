"""
Python Solution
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def sum_at_node(root: Optional[TreeNode], d: dict) -> int:
            if root is None:
                return 0
            val = root.val + sum_at_node(root.left, d) + sum_at_node(root.right, d)
            d[root] = val
            return val
            
        # Dictionary to store the sum of subtree with current node as root
		# {Node: Sum of subtree with Node as root}
        d = {}
        sum_at_node(root, d)
        ans = 0
        root_val = d[root]
        for i,v in d.items():
            ans = max(ans, (root_val - v) * v)
        
        return ans % int(1e9+7)
