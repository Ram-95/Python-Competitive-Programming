class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        prev = 1
        for i in nums:
            if i == prev:
                prev += 1
        return prev
