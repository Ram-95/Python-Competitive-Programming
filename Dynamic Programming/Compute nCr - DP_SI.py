#Compute nCr - Dynamic Programming Smart Interviews
from sys import stdin, stdout
N = 2000

global mod
mod = int(1e9+7)

global dp
dp = [-1]*(N+1)
(dp[0],dp[1]) = (1,1)


for i in range(2,N+1):
    if dp[i] == -1:
        dp[i] = ((i) * (dp[i-1]))


def ncr(n,r):
    val = dp[n]//(dp[n-r] * dp[r])
    return val % mod


t = int(stdin.readline())
while t:
    nr = list(map(int, stdin.readline().rstrip().split()))
    n = nr[0]
    r = nr[1]
    stdout.write(str(ncr(n,r)) + '\n')
    t = t - 1

'''
Giving TLE - Check Method 2 [Discussed in the class]
'''
