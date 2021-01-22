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
        

'''My Solution O(N) Time and Space.'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        a = ord('a')
        s1 = set(word1)
        s2 = set(word2)
        
        for i in word1:
            count1[ord(i) - a] += 1
        
        for i in word2:
            count2[ord(i) - a] += 1
         
        count1.sort()
        count2.sort()
            
        return count1 == count2 and s1 == s2
        
