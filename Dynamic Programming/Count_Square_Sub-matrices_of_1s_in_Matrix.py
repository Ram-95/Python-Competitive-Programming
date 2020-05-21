



'''
Leetcode question. 
Given a Matrix of size M x N, you have to find out the 
total number of square sub-matrices that have all 1s in 
them. 
1. Solved Using DP - O(MN) Time and Space
2. DP State dp[i][j] = The number of square sub-matrices that end at dp[i][j].
3. DP Expresion dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) if matrix[i][j] == 1
else 0
4. Finally return the answer i.e, SUM of the dp matrix. 
'''

class Solution:
    def countSquares(self, arr: List[List[int]]) -> int:
        (m,n) = (len(arr), len(arr[0]))
        dp = [[0 for i in range(n)] for i in range(m)]
        sums = 0
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    sums += dp[i][j]
                
        
        return sums







