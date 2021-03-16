# Dynamic Programming

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buying, selling = 0, -prices[0]
        for i in range(1, len(prices)):
            buying = max(buying, selling + prices[i] - fee)
            selling = max(selling, buying - prices[i])
        return buying
