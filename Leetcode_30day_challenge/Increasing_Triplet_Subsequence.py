# Solution - 1: Time: O(N)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Set both the first and the second values as MAX value
        first = second = float('inf')
        
        for i in nums:
            if i <= first:  # This will ensure that we always store the minimum value in first
                first = i
            elif i <= second:   # This will ensure that we always store a value greater than first
                second = i
            else:   # If we have reached here, we have seen a value greater than first and second. So return True
                return True
        
        return False
