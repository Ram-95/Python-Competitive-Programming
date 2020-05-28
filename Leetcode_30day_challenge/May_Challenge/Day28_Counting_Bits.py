#Given a Number find the no. of 1s from 0 to that number and return the array.
#Normal approach is O(N * 32). You need to do this in O(N).
#The Recurrence equation is 
# 1. arr[i] = arr[i>>1] + (i&1) -- Using Bitwise Operators.
# 2. arr[i] = arr[i//2] + i % 2 -- Using Arithmetic Operators.

class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0 for i in range(num+1)]
        for j in range(1,num+1):
            ans[j] = ans[j >> 1] + (j&1)
        
        return ans
        
