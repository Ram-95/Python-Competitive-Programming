# From the problem definition, we know that all local inversions are global inversions. So if we could find any inversion that is global and not local, then problem is solved.
# That is if we can find any A[i] > A[j] where j >= i+2, then answer is False.
# So we iterate till (n-2)th element, maintain a max_element we have seen so far and check if there exists any 'i+2'th element that is less than max number
# seen so far. If exists return False

''' O(N) Time. '''
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        gi, li = 0, 0
        n = len(A)
        maxm = 0
        # All local inversions are also global inversions
        for i in range(n-2):
            maxm = max(maxm, A[i])
            # if we see any 'i+2' th element greater than current maximum, then it is a
            # global inversion and not a local inversion. So return False.
            if maxm > A[i+2]:
                return False
        
        return True
        
        
