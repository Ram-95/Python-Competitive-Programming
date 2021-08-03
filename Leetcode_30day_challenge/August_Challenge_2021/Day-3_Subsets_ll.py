class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def generate(arr, idx, subarr, res):
            if idx == len(arr):
                if len(subarr) > 0:
                    # To avoid adding duplicates
                    res.add(tuple(sorted(subarr)))
                return
            # Not including the element at current index - idx
            generate(arr, idx + 1, subarr, res)
            # Including the element at current index - idx
            generate(arr, idx + 1, subarr + [arr[idx]], res)
        
        res = set()
        generate(nums, 0, [], res)
        l = [list(x) for x in res] + [[]]
        
        return l        
            
        
