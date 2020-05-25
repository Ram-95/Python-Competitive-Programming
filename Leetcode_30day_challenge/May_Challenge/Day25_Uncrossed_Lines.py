## This is same as solving LCSS - Longest Common Sub Sequence.

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        #columns
        m = len(A)
        #rows
        n = len(B)
        
        #Creating a DP Matrix of size [n+1][m+1] with all Zeros initially to store the answers
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        #Filling the DP matrix - The logic is same as the LCSS - Longest Common Subsequence.
        for i in range(1,n+1):
            for j in range(1,m+1):
                if B[i-1] == A[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        #The answer is stored at the end of the DP Matrix.
        return dp[n][m]
        
