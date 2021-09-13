class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = set('balloon')
        d = {}
        
        for i in text:
            d[i] = d.get(i,0) + 1
        
        #print(d)
        ans = 0
        while True:
            for i in 'balloon':
                if i not in d or d[i] < 1:
                    return ans
                else:
                    d[i] -= 1
            ans += 1
            
        
        return ans
