# https://leetcode.com/problems/path-sum/
'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
Solution: O(N) Time and O(Height) Space
'''

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def solve(root, sums):
            if root is None:
                return False
            
            if root.left is None and root.right is None and root.val == sums:
                    return True
            sums -= root.val
            return solve(root.left, sums) or solve(root.right, sums)
            
        
        res = solve(root, targetSum)
        return res
