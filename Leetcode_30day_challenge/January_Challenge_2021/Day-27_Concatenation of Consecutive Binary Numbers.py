''' My Solution '''
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ''
        MOD = int(1e9+7)
        for i in range(1,n+1):
            s += bin(i)[2:]
        
        return int(s,2) % MOD
            
        
