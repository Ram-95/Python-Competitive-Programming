''' My Solution - Sliding window searching using deque'''
from collections import deque
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        '''For every item in pieces search the item in arr the window of size len(item)'''
        for i in pieces:
            if not search(arr, i):
                return False
        return True
    
def search(arr, val):
    '''Returns true if val(window) is present in arr.'''
    # length of the window
    sz = len(val)
    d = deque(maxlen=sz)
    for i in arr:
        d.append(i)
        if list(d) == val:
            return True
    return False
    
   
''' Best Solution - No additional space'''
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            try:
                idx = arr.index(piece[0])
            except:
                return False
            if arr[idx:idx+len(piece)]!=piece:
                return False
        return True
