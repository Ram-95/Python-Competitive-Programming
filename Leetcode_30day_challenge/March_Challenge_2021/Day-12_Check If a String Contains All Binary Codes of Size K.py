''' My Solution - O(NK) Time and O(2^K) Space. '''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary = []
        maxm = (1 << k)
        # Generates all the binary codes of length 'k'
        for i in range(maxm):
            #print(bin(i).zfill(k))
            binary.append(bin(i)[2:].zfill(k))
        
        for i in binary:
            if i not in s:
                return False
            
        return True
      
      
''' A bit of optimization. '''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return 1<<k<=len(s) and len({s[i:i+k] for i in range(len(s)-k+1)})==1<<k
        
