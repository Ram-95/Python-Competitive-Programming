class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Base Condition
        if n == 0:
            return False
        #This Bitwise operation will unset the right most set bit.
        elif n & (n-1) == 0:
            return True
        return False
        
