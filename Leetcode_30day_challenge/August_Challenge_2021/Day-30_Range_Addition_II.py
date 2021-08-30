#########
# The maximum value is present in between [0, min(a)] and [0, min(b)]. So return min(a) * min(b) for all the items in "ops" list.
# Special Case: When ops is empty, then the answer is 0 and the number of 0's is nothing but m * n
#########

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:    
        # Case when ops = []
        if not ops:
            return m * n
        min_a, min_b = float('inf'),float('inf')
        for i in ops:
            min_a = min(i[0], min_a)
            min_b = min(i[1], min_b)
        
        return min_a * min_b
