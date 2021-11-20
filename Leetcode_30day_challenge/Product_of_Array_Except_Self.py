# Solution - 1: Time: O(N) and Space: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suff = [nums[0]], [nums[-1]]
        n = len(nums)
        # Calculating the Prefix Product
        for i in range(1, n):
            pre.append(pre[-1] * nums[i])
        
        # Calculating the Suffix Product
        for j in range(n-2,-1,-1):
            suff.append(suff[-1] * nums[j])
        suff.reverse()
        
        ans = [0] * n
        ans[0] = suff[1]
        for i in range(1, n-1):
            ans[i] = pre[i-1] * suff[i+1]
        
        ans[n-1] = pre[n-2]        
        
        return ans
