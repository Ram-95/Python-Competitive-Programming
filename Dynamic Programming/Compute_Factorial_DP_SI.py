#Compute Factorial using Dynamic Programming - Smart Interviews
#Precompute and answer each test case

#Precomputing the Dp Array
N = 1000000
mod = int(1e9+7)

dp = [-1]*(N+1)
(dp[0],dp[1]) = (1,1)


for i in range(2,N+1):
    if dp[i] == -1:
        dp[i] = ((i % mod) * (dp[i-1] % mod)) % mod


t = int(input())
while t:
    n = int(input())
    print(dp[n])
    t = t - 1
