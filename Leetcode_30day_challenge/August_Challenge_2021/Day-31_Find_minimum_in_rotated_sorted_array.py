# Linear Search - O(N)
# Binary Search - O(logN)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Special cases
        # If only one element
        if len(nums) == 1:
            return nums[0]
        # If not rotated. How do we know ? If nums[0] < nums[n-1]
        if nums[0] < nums[-1]:
            return nums[0]
        
        # Binary Search
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] < nums[low]:
                # Check for inflection point on the left side
                high = mid - 1
            else:
                # Check for inflection point on the right side
                low = mid + 1
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
