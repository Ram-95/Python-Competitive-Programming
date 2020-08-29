class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans=[]
        i=0
        for x in range(len(A),1,-1):
            max_index=A.index(x)
            ans.extend([max_index+1,x])
            A=A[:max_index+1][::-1]+A[max_index+1:]
            A=A[x-1::-1]+A[x:]
        return ans
        
