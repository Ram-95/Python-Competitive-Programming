class Solution:
    def titleToNumber(self, s: str) -> int:
        d = {}
        for i in range(65, 91):
            d[chr(i)] = i - 65 + 1
        n = len(s)
        #print(d)
        if n == 1:
            return d[s]
        ans = d[s[0]]
        for i in range(n-1):
            ans = ans * 26
            ans += d[s[i+1]]
            #print(ans)
            
        
        
        
        return ans
        
        
