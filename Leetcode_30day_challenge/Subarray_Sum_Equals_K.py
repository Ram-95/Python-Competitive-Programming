class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, pre = 0, 0
        d = {}    
        for i in nums:
            pre += i
            
            if pre == k:
                ans += 1
            
            if pre - k in d:
                ans += d[pre-k]
            
            if pre not in d:
                d[pre] = 1
            else:
                d[pre] += 1
            
        
        return ans
