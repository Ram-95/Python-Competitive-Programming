'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''

#Method 1 - Linear - Time - O(N)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] >= target:
                return i
        
        #If the target is greater than max of array
        return n

#Method 2 - Binary Search - Time - O(Log N)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return low
           
