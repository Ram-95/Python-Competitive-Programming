from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d = Counter(arr)
        arr.sort(key=abs)
    
        for i in arr:
            double = 2*i
            if d[i] == 0:
                continue
            if d[double] == 0:
                return False
            d[double] -= 1
            d[i] -= 1
            
        return True
