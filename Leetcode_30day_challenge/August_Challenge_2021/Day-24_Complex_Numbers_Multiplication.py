class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = num1.split('+')
        c,d = num2.split('+')
        a,c = int(a), int(c)
        b,d = int(b.strip('i')), int(d.strip('i'))
        
        ans = str(a*c - d*b) + '+' + str(a*d+b*c) + 'i'
        
        return (ans)
       
