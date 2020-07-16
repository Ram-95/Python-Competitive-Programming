#Longest Common Subsequence - Dynamic Programming
def lcss(A, B):
    m = len(A)
    n = len(B)
    #Creating a DP matrix - NxM Size
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n):
        for j in range(m):
            if B[i] == A[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #print(dp)
    return dp[n-1][m-1]
    


print(lcss('abbcdgf', 'bbadcgf'))
