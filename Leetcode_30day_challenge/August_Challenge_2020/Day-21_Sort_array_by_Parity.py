'''
Q: Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''
# My Solution - O(N) Space
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        d = {'even': [], 'odd': []}
        for i in A:
            if i&1 == 0:
                d['even'].append(i)
            else:
                d['odd'].append(i)
        
        ans = d['even'] + d['odd']
        return ans

    
#Two Pointer - Inplace O(1) Space
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #Two pointer approach
        p1, p2 = 0, len(A)-1
        while p1 < p2:
            if A[p1] & 1 > A[p2] & 1:
                # Swapping
                A[p1], A[p2] = A[p2], A[p1]
            
            if A[p1] & 1 == 0:
                p1 += 1
            if A[p2] & 1 == 1:
                p2 -= 1
        
        return A
