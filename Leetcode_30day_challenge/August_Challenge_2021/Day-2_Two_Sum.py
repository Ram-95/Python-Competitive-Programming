''' Brute Force solution - O(N^2) '''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            for j,vs in enumerate(nums[i+1:], i+1):
                if v +  vs == target:
                    return [i, j]
            

''' Optimized O(N) Time and O(N) Space. '''

# Two pass Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keys are the value of nums, Values is a list = [frequency, Indices....]
        d = {}
        for i,v in enumerate(nums):
            if v not in d:
                d[v] = [1, i]
            else:
                d[v][0] += 1
                d[v].append(i)
        
        for i in nums:
            value = target - i
            if value == i and d[value][0] > 1:
                return d[value][1:3]
            elif value in d and value != i:
                return [d[i][1], d[value][1]]            
                
            
            
# One Pass Solution
'''While inserting the element in dictionary itself, we check if (target - i) is already present in dict. If present return the indices there itself.'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(nums):
            value = target - v
            if value in d:
                return [d[value], i]
            else:
                d[v] = i
        
