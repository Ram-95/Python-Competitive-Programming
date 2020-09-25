import functools 

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        compare = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        _nums = list(map(str, nums))
        _nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        return str(int(''.join(_nums)))
