'''
Python Solution - Using Dictionary and Compare function
Time: O(N*w) ; where N = No. of words and w: length of each word
Space: O(1)
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)):
            d[order[i]] = i+1
        
        # Compare function to know if two strings are lexicographically ordered
        def compare(s1, s2, d):
            p1, p2 = 0, 0
            n1, n2 = len(s1), len(s2)
            while p1 < n1 and p2 < n2:
                chr1, chr2 = d[s1[p1]], d[s2[p2]]
                if chr1 == chr2:
                    p1 += 1
                    p2 += 1
                elif chr1 > chr2:
                    return False
                elif chr1 < chr2:
                    return True
            
            # If s2 is a proper prefix of s1, then lexicographically s1 > s2
            if (p1 < n1 and p2 >= n2):
                return False
            
            return True
        
        # Iterating over the words and checking if they're lexicographically ordered
        for i in range(len(words)-1):
            if not compare(words[i], words[i+1], d):
                return False
        
        return True
