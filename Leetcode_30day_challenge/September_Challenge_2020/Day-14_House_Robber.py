# Method 1
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = 0, 0
        for i in range(n):
            if i % 2 == 0:
                a = max(a + nums[i], b)
            else:
                b = max(a, b + nums[i])
        
        return max(a,b)

#Method - 2 Can be done using DP. Deduce the dp expression       
