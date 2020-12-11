class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        size = len(arr)
        if size == 1:
            return False
        
        # Two pointer method - One person climbing from start and the other end
        p,q,r = (0,size-1,size)
        
        while p+1 < size and arr[p] < arr[p+1]:
            p += 1
        
        while q > 0 and arr[q] < arr[q-1]:
            q -= 1
        
        # If p == q and they lie between first and last element exclusive
        return 0 < p == q < size-1
            
