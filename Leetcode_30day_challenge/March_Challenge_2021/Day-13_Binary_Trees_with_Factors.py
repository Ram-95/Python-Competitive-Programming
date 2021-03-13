''' My Solution - O(N^2) Time and O(N) Space. '''

class Solution:
     def numFactoredBinaryTrees(self, A):
        dp = {}
        MOD = int(1e9+7)
        # dp(x) is the no. of ways to make a tree with root node 'x'.
        # if a * b == x, then 'a' and 'b' can be the children of node 'x' and the
        # no. of ways to make this tree is dp(a) * dp(b)
        
        for a in sorted(A):
            dp[a] = sum(dp[b] * dp.get(a / b, 0) for b in dp if a % b == 0) + 1
        #print(dp)
       
        return sum(dp.values()) % MOD
        
