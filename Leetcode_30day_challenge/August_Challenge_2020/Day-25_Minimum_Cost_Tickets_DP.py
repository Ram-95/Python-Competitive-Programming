''' Question: https://leetcode.com/problems/minimum-cost-for-tickets/
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

'''


class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        last = days[-1] + 1
        # Converting the days array to a set for faster lookup O(1)
        days = set(days)
        
        # DP array - Stores the answer till i'th Day
        dp = [0 for i in range(last)]
        
        for i in range(last):
            if i not in days:
                dp[i] = dp[i-1]
            # We need the minimum cost of all days - 1,7 and 30 Days
            else:
                dp[i] = min(dp[max(0,i-7)] + cost[1], dp[max(0, i-1)] + cost[0], dp[max(0,i-30)] + cost[2])
        
        # Returning the answer - The last item in dp array.
        return dp[-1]
                
        
