''' My Solution - O(amount * len(coins)) Time and O(amount) Space. '''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP array
        dp = [float('inf') for _ in range(amount)]
        
        # Inserting 0 at the start of DP array to handle the case where amount = 0
        dp.insert(0,0)
        
        for i in range(1, amount+1):
            for j in coins:
                if i >= j:
                    # DP expression
                    dp[i] = min(dp[i], dp[i-j] + 1)
        
        return -1 if dp[-1] == float('inf') else dp[-1]
