
def collect_apples(arr,n,m):
    #DP table
    dp = [[None for i in range(m+1)] for j in range(n+1)]

    #Base Conditions
    #marking the first row as all 0s
    for i in range(m+1):
        dp[0][i] = 0

    #marking the first column as all 0s
    for j in range(n+1):
        dp[j][0] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            #DP Expression -> Maximum #apples taken till arr[i][j](including arr[i][j])
            dp[i][j] = max(dp[i][j-1] + arr[i-1][j-1], dp[i-1][j] + arr[i-1][j-1])

    #print(dp)
    return dp[n][m]
    
    
    
    
t = int(input())
while t:
    nm = list(map(int, input().rstrip().split()))
    n = nm[0]
    m = nm[1]
    arr = []
    for _ in range(n):
        temp = list(map(int, input().rstrip().split()))
        arr.append(temp)
    print(collect_apples(arr,n,m))        
    t = t - 1
