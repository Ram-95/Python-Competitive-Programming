class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Min and Max arrays
        mn, mx = [], []
        n = len(prices)
        temp = float('inf')
        # Filling the Minimum element seen so far
        for i in prices:
            mn.append(min(temp, i))
            temp = mn[-1]
        #print(mn)
        temp = float('-inf')
        # Filling the Maximum element seen so far
        for i in prices[::-1]:
            mx.insert(0,max(temp, i))
            temp = mx[0]
        #print(mx)
        ans = 0
        
        # Find the max difference of the minimum and maximum arrays
        for i in range(n):
            ans = max(ans, mx[i]-mn[i])
        
        return ans
        
