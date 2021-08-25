# Solution - 1: PreComputation
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        threshold = (1<<31) - 1
        pre = set()
        i = 0
        while True:
            temp = i*i
            if temp > threshold:
                break
            else:
                pre.add(temp)
            i += 1
            
        for i in pre:
            val = c - i
            if val in pre:
                return True
        
        return False



# Solution - 2
import math
class Solution:
        
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c))+1):
            b = math.sqrt(c - a*a)
            if b == int(b):
                return True
        
        return False
