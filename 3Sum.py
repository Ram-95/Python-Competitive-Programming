# Solution - 1 | O(N**2) Time and O(N) Space
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
            if left > 0 and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
                continue 
            mid = left + 1 # renamed this to mid because this is the pointer that is between the left and right pointers
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum < 0:
                    mid += 1 
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                        right -= 1
                    mid += 1
                    right -= 1
        return result
                        
        



# Solution - 2 | O(N**2) Time and O(N) Space
from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        ans, n = set(), len(nums)
        def two_sum(arr, target):
            c = Counter(arr)
            res = set()
            for i in arr:
                x = target - i
                if x in c:
                    if x == i and c[x] > 1:
                        if (i,x) not in res and (x,i) not in res:
                            res.add((i, x))
                    elif x != i:
                        if (i,x) not in res and (x,i) not in res:
                            res.add((i, x))                    
            return res
        
        
        for i,v in enumerate(nums):
            if v not in visited:
                t_arr = nums[:i] + nums[i+1:]
                ts = two_sum(t_arr, -v)
                if ts:
                    for item in ts:
                        t = [v] + list(item)
                        t.sort()
                        ans.add(tuple(t))
                visited.add(v)
            
        return ans
