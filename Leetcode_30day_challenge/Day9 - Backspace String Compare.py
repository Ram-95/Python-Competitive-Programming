#Day-9 Backspace String Compare

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        x = ''
        y = ''
        flag = 0
        
        i = len(S) - 1
        while i >= 0:
            if S[i] == '#':
                flag += 1
                i -= 1
            else:
                if flag == 0:
                    x += S[i]
                    
                else:
                    flag -= 1
                i -= 1
            
          
       
        j = len(T) - 1
        flag = 0
        
        while j >= 0:
            if T[j] == '#':
                flag += 1
                j -= 1
            else:
                if flag == 0:
                    y += T[j]
                else:
                    flag -= 1
                j -= 1
            
           
            
         
        if x == y:
            return True
        return False
