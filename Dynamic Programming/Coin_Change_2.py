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
        
                    
        
        
