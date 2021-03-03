''' My Solution - O(N) Time and O(1) Space. '''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sums = (n*(n+1))//2
        return sums - sum(nums)
        
