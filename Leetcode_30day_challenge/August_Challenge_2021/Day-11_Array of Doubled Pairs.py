from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d = Counter(arr)
        arr.sort(key=abs)
    
        for i in arr:
            double = 2*i
            # Since we have sorted the array, we'll first iterate over the small values and if small values frequency is zero, we just continue
            if d[i] == 0:
                continue
            # If double values frequency is Zero, that means there is no double value for i. So we return False    
            if d[double] == 0:
                return False
            # Decrement both i and double
            d[double] -= 1
            d[i] -= 1
            
        return True
