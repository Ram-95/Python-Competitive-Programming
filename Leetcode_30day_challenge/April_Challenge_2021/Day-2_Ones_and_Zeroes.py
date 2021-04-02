# Refer: https://leetcode.com/problems/ones-and-zeroes/discuss/95808/0-1-knapsack-in-python

class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range (m + 1)]
        
        for s in strs:
            m1, n1 = s.count('0'), s.count('1')
            for i in range(m, m1 - 1, -1):
                for j in range(n, n1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - m1][j - n1] + 1)
        
        return dp[m][n]
