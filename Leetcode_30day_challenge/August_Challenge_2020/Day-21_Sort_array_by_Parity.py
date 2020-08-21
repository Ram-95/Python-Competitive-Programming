'''
Q: Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''

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
                
