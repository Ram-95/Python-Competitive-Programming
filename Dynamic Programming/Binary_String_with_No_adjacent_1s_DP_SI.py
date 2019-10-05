#Binary String with no adjacent 1's - Dynamic Programming Smart Interviews
global dp0, dp1
mod = int(1e9+7)
N = 100000

#DP Tables
dp0 = [-1]*N
dp1 = [-1]*N

#Base Conditions
dp0[0] = 1
dp1[0] = 1

#Precomputing the DP arrays
for i in range(1,N):
    dp0[i] = (dp0[i-1] % mod + dp1[i-1] % mod) % mod
    dp1[i] = dp0[i-1]

t = int(input())
while t:
    n = int(input())
    print((dp0[n-1] + dp1[n-1]) % mod)
    t = t - 1

    
