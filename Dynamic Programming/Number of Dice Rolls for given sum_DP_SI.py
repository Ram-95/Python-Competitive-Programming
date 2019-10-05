#Number of Dice Rolls for given sum - Dynamic Programming Smart Interviews

from sys import stdin, stdout

N = 100000
mod = int(1e9+7)
global dp
dp = [0]*(N+1)

#Base Condition
dp[0] = 1

#Precomputing the DP Array values
#Each dp[i] indicates the no.of ways we can get the sum 'i'
for i in range(1,N+1):
    sums = 0
    for j in range(1,7):
        if i - j >= 0:
            sums += dp[i-j]

    dp[i] = sums % mod




t = int(input())
while t:
    n = int(stdin.readline())
    stdout.write(str(dp[n] % mod) + '\n')
    t = t - 1

