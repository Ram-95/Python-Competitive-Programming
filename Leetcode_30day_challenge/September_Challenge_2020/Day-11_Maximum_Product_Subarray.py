'''
# Method: 
Calculate prefix product and suffix product in given array.
Return the max of those two.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Reversing the given array. Used to calculate the Suffix product
        temp = nums[::-1]
        for i in range(1, len(nums)):
            # Calculating the Prefix Product
            nums[i] *= nums[i-1] or 1
            # Calculating the Suffix Product
            temp[i] *= temp[i-1] or 1
        
        # Return the maximum of Prefix and Suffix Products
        return max(nums + temp)
