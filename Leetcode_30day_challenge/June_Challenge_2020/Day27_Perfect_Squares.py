'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
'''

import math
def solve(n):
    if n == 0:
        return 0
    dp = [0]
    INT_MAX = 1 << 31

    while len(dp) <= n:
        size =  len(dp)
        temp = INT_MAX
        for i in range(1,math.floor(math.sqrt(size)) + 1):
            temp = min(temp, dp[size - (i*i)]+1)

        dp.append(temp)

    return dp[n]

print(solve(7))
