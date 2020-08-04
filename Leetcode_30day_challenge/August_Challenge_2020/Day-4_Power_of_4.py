### Q: Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Using Loops
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        
        binary = bin(num)[2:]
        ones = binary.count('1')
        if ones != 1:
            return False
        else:
            zeros = 0
            flag = 0
            for i in binary:
                if i == '1':
                    flag = 1
                if flag == 1 and i == '0':
                    zeros += 1
            
        return zeros%2 == 0
               
        
# O(1) - One Liner
'''
If Number is Positive AND it is power of 2 AND (num-1) is a multiple of 3 then return True. Else return False
'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and (num-1)%3 == 0
    
        
