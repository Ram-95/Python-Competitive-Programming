#0/1 The Knapsack Problem - Dynamic Programming Smart Interviews

def knapsack(N,S,p,w):
    dp = [[-1 for i in range(S+1)] for j in range(N+1)]

    #Making the first row all zeros
    
    for k in range(S+1):
        #print(k)
        dp[0][k] = 0

    for i in range(1,N+1):
        for j in range(S+1):
            if j >= w[i-1]:
                dp[i][j] = max(dp[i-1][j-w[i-1]] + p[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    #print(dp)
    return dp[N][S]


t = int(input())
while t:
    sn = list(map(int, input().rstrip().split()))
    #Capacity of the bag
    s = sn[0]
    #No of items
    n = sn[1]

    #Profit array
    p = []
    #Weight Array
    w = []
    n_t = n
    while n:
        arr = list(map(int, input().rstrip().split()))
        w.append(arr[0])
        p.append(arr[1])
        n = n - 1
    print(knapsack(n_t,s,p,w))
    
    t = t - 1
