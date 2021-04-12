class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        arr = list(range(1,n-k))
        
        for i in range(k+1):
            if i&1:
                arr.append(n-(i//2))
            else:
                arr.append(n-k+(i//2))
         
        return arr
        
