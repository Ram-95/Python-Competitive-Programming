class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        (left, right) = (0,0)
        
        for i in range(n):
            if s[i] in '(*':
                left += 1
            else:
                left -= 1
                
            if s[n-i-1] in ')*':
                right += 1
            else:
                right -= 1
                
            if left < 0 or right < 0:
                return False
            
        return True   
        
