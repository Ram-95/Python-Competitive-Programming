#Subset Sum Problem/ Coin Change - Dynamic Programming Smart Interviews
def Coin_Change(arr, n, s):
    #DP Table
    dp = [[False for i in range(s+1)] for j in range(n+1)]

    #Making the first row all 'False'
    for k in range(s+1):
        dp[0][k] = False

    #Making the first column 'True' - Meaning we can always get a Sum of Zero{If we don't choose any item}
    for p in range(n+1):
        dp[p][0] = True

    #print('DP: {}'.format(dp))

    for i in range(1,n+1):
        for j in range(s+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            elif j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j-arr[i-1]]) or (dp[i-1][j])

    return dp[n][s]


t = int(input())
while t:
    (n,s) = (map(int, input().split()))
    arr = list(map(int, input().rstrip().split()))
    print(['No', 'Yes'][Coin_Change(arr, n, s)])
    t = t - 1
