'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
'''

#This Solution is based on - Dutch national flag problem

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        w,r,b = 0,0,len(nums)-1
        
        while w <= b:
            if nums[w] == 0:
                #If it is RED Colour, Swap them
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
            elif nums[w] == 1:
                #If it is WHITE, it is at its correct position only, Just increase W pointer
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
        
