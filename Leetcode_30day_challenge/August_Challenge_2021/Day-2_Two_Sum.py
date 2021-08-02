''' Brute Force solution - O(N^2) '''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            for j,vs in enumerate(nums[i+1:], i+1):
                if v +  vs == target:
                    return [i, j]
            

''' Optimized O(N) Time and O(N) Space. '''

# Iterating Twice - O(2*N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        # O(N)
        for i,v in enumerate(nums):
            d[v] = i
        # O(N)
        for i,v in enumerate(nums):
            value = target - v
            if value in d and d[value] != i:
                return [i, d[value]]
        
            
            
# Iterating Once - O(N)
'''While inserting the element in dictionary itself, we check if (target - i) is already present in dict. If present return the indices there itself.'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        # O(N)
        for i,v in enumerate(nums):
            value = target - v
            if value in d:
                return [d[value], i]
            else:
                d[v] = i
        
