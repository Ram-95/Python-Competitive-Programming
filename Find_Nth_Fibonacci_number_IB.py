#Find Nth_Fibonacci Number
'''
************* My Approach - DP ************
N = 100000
mod = int(1e9 + 7)
dp = [0] * N
#Base Conditions
dp[0], dp[1] = 1, 1

for i in range(2, N):
    dp[i] = dp[i-1] + dp[i-2]

n = int(input('Enter n: '))
print(dp[n] % mod)
    
'''

## This Method is based on Formula - [Source: http://codeforces.com/blog/entry/18292?]
mod = int(1e9+7)
d = {}

def fib(n):
    if n < 2:
        return 1
    if n in d:
        return d[n]
    d[n] = (fib((n+1)//2)*fib(n//2) + fib((n-1)//2)*fib((n-2)//2)) % mod

    return d[n]

n = int(input('Enter N: '))
print(fib(n))

            
