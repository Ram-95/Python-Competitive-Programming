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

# Solution - 2: Time: O(N) Time and O(1) Space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = nums.count(0)
        prod = 1
        ans = [0]*n
        zero_idx = None
        # Calculating the Product
        for i,v in enumerate(nums):
            if v != 0:
                prod *= v
            else:
                zero_idx = i

        if c > 1:
            return ans
        elif c == 0:
            for i in range(n):
                ans[i] = prod//nums[i]
        else:
            ans[zero_idx] = prod
            
        return ans
