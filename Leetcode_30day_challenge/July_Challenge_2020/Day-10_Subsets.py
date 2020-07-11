'''Using Powerset function from Itertools'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def powerset(iterable):
            '''Returns the PowerSet of a given set'''
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
        
        x = powerset(nums)
        x = [list(item) for item in x]
    
        return x
        
        
''' Method 2 '''

def subsets(nums):
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
      
print(subsets([1,2,3]))
