''' https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3446/
Hint: Use Sliding Window and Sorting
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k < 1:
            return False
        d = collections.OrderedDict()
        
        for i in nums:
            key = i if not t else i//t
            for m in (d.get(key-1), d.get(key), d.get(key+1)):
                if m is not None and abs(i-m) <= t:
                    return True
            if len(d) == k:
                d.popitem(False)
            d[key] = i
            
        return False
