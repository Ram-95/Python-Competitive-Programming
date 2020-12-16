# Using Deque - O(N) Time and Space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        d = collections.deque()
        p1,p2 = 0, len(nums)-1
        while p1 <= p2:
            if abs(nums[p1]) > abs(nums[p2]):
                d.appendleft(nums[p1]**2)
                p1 += 1
            else:
                d.appendleft(nums[p2]**2)
                p2 -= 1
        
        return d


# Normal using Sort - O(NlogN) Time and O(1) Space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x*x for x in nums]
        nums.sort()
        
        return nums
