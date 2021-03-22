
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        s = set()
        for i in range(30):
            val = 1 << i
            s.add(tuple(sorted(str(val))))
        #print(s)
        num = tuple(sorted(str(N)))
        
        return num in s
