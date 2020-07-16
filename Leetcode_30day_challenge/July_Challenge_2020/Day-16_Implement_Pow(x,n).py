class Solution:
    def myPow(self, a: float, b: int) -> float:
        sign = b//1
        b = abs(b)
        x = a
        ans = 1
        while b:
            if b&1:
                ans = ans * x
            b = b >> 1
            x = x * x
            #print(f'x :{x}')
            #print(f'ans: {ans}')
            
        return ans if sign >= 0 else 1/ans
            
