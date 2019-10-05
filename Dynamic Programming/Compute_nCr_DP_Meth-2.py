#Compute nCr - Dynamic Programming

from sys import stdin, stdout

(N,R) = (2000,2000)

global dp
dp = [[-1 for i in range(N+1)] for j in range(R+1)]

for i in range(N+1):
    dp[i][0] = 1

for j in range(1,R+1):
    dp[0][j] = 0

for i in range(1,N+1):
        for j in range(1,R+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


def solve(n,r):
    mod = int(1e9+7)
    return dp[n][r] % mod
    
    

t = int(stdin.readline())
while t:
    nr = list(map(int, stdin.readline().rstrip().split()))
    n = nr[0]
    r = nr[1]
    stdout.write(str(solve(n,r)) + '\n')
    t = t - 1
        
