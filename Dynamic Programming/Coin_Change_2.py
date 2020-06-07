'''
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        n = len(coins)

        dp = [0] * (amount+1)
        m = len(dp)
        #Base Condition - The no. of ways to get sum 0 is always 1.
        dp[0] = 1
        
        for i in range(n):
            for amt in range(1,amount+1):
                if amt >= coins[i]:
                    dp[amt] += dp[amt - coins[i]]
        
        #print(dp)
        return dp[amount]
        
                    
        
        
