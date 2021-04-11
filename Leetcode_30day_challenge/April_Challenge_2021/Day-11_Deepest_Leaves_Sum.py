# Solution - 1: Recursion - O(N) Time and Space.
class Solution:
    def __init__(self):
        self.res = 0
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # Function to find the depth of the Tree
        def depth(root):
            if root is None:
                return 0
            lst = depth(root.left)
            rst = depth(root.right)
            if lst > rst:
                return lst+1
            else:
                return rst+1
                
        # Function to find the sum of deepest nodes values
        def sum_deep_leaves(root, curr_dep, ans, max_depth):
            if root is None:
                return 0
            if curr_dep == max_depth:
                    self.res += root.val
            sum_deep_leaves(root.left, curr_dep+1, ans, max_depth)
            sum_deep_leaves(root.right, curr_dep+1, ans, max_depth)
        
        x = depth(root)
        sum_deep_leaves(root, 0, 0, x-1)
        
        return self.res

    
# Solution - 2: Using Queue | O(N) Time and Space.
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = 0
        # Base Condition
        if root is None:
            return 0
        
        q = [root]
        # Keep adding the child level after level
        while True:
            # Add the left child
            q_new = [x.left for x in q if x.left]
            # Add the right child
            q_new += [x.right for x in q if x.right]
            # If q_new is empty, that means we have reached the end of all levels of tree
            if not q_new:
                break
            # Make the current level as previous
            q = q_new
        
        # Sum up all the values of the last level and return the answer
        for i in q:
            ans += i.val
        return ans
        
        
