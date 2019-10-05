
def path_in_matrix(mat, n, m):
    mod = int(1e9+7)

    #DP Table/Matrix - Copying the matrix as a DP Table
    dp =[m[:] for m in mat]
    
    '''Base Conditions'''
    #If the Source OR Destination are blocked, then there is NO way.
    if mat[0][0] == 0 or mat[n-1][m-1] == 0:
        return 0
    
    if mat[n-2][m-1] == 0:
        dp[n-2][m-1] = 0
    else:
        dp[n-2][m-1] = 1

    if mat[n-1][m-2] == 0:
        dp[n-1][m-2] = 0
    else:
        dp[n-1][m-2] = 1
    
    dp[n-1][m-1] = 1

    #print('DP1: {}'.format(dp))

    #DP Expression and DP Matrix Computation
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            #If Cell is blocked, then there is no way to reach that cell. Hence, a ZERO.
            if mat[i][j] == 0:
                dp[i][j] = 0
            else:
                #print('i: {}  j: {}'.format(i,j))
                dp[i][j] = dp[i+1][j] + dp[i][j+1] + dp[i+1][j+1]
    #print('DP: {}'.format(dp))
    return dp[0][0] % mod
        



t = int(input())
while t:
    #Flags to know if there is a blocked cell in the last row(fr) or column(fc)
    (fr,fc) = (0,0)
    
    (n,m,b) = (map(int, input().split()))
    #Initially setting all values of the matrix as 1.
    mat = [[1 for i in range(m)] for j in range(n)]

    while b:
        (i,j) = (map(int, input().split()))
    
        #Making the Last row/column values till the blocking cell(including that cell) as '0'{Not Reachable}
        if i == n-1 and j == m-1:
            mat[i][j] = 0
        elif i == n-1:
            for idx in range(j+1):
                mat[i][idx] = 0
        elif j == m-1:
            for idx1 in range(i+1):
                mat[idx1][j] = 0
        else:
            mat[i][j] = 0
        b = b - 1
    #print('Matrix: {}'.format(mat))
    print(path_in_matrix(mat, n, m))
    t = t - 1
