''' My Solution - O(N) Time and O(1) Space.'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for j in t:
            if j in d:
                d[j] -= 1
            else:
                d[j] = 1
        
        for i in d.values():
            if i != 0:
                return False
        return True
        
