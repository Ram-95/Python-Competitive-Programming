#Stairs - Dynamic Programming

def stairs(n):
    #DP Table
    dp = [None]*(n+1)

    #Base Conditions
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
    



n = int(input('N: '))
print(stairs(n))
