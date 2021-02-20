class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'M': 1000, 'D': 500}
        n = len(s)
        prev = '$'
        ans = 0
        if n == 1:
            return d[s]
    
        for i in range(n-1,-1,-1):
            if s[i] == 'I' and prev in 'VX':
                ans += -1
            elif s[i] == 'X' and prev in 'LC':
                ans += -10
            elif s[i] == 'C' and prev in 'DM':
                ans += -100 
            else: 
                ans += d[s[i]]
            
            prev = s[i]
            #print(f'Ans: {ans}')
      
        return ans
            
            
        
        
