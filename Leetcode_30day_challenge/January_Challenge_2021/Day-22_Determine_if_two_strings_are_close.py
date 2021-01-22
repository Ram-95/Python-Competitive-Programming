#My solution - O(NlogN) Time and O(N) Space.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d = {}
        d2 = {}
        
        for i in word1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in word2:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
        

        keys1 = sorted(list(d.keys()))
        keys2 = sorted(list(d2.keys()))
        val1 = sorted(list(d.values()))
        val2 = sorted(list(d2.values()))
        
        return keys1 == keys2 and val1 == val2
        
