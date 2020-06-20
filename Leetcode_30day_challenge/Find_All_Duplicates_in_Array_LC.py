'''
Question: Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''

#Optimal Solution - Time and Space - O(N) and O(1)
#Other Solution is using a set - Time and Space - O(N) and O(N)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #List to store the answer
        ans = []
        
        #Making the numbers at nums[nums[i] -1 ] as negative. 
        #In the loop if we see that a number at an index is already negative, then that
        #number is occuring twice - Append that number to 'ans' array
        
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
            elif nums[val] < 0:
                ans.append(val+1)
        
        return ans
