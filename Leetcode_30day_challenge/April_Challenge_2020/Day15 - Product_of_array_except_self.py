class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left = nums[0]
        right = nums[-1]
        
        for i in range(1,n):
            ans[i] = left
            left *= nums[i]
        #print(ans)
        for j in range (n-2,-1,-1):
            ans[j] *= right
            right *= nums[j]
            
        return ans
