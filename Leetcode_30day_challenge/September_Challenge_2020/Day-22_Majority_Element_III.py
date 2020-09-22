class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = collections.Counter(nums)
        ans = []
        for i,v in d.items():
            if v > n//3:
                ans.append(i)
        
        return ans
        
