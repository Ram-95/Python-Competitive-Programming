# O(N) Time and O(1) Space

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        
        def check(a, b):
            d = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
            a_count, b_count = 0, 0
            for i in a:
                if i in d:
                    a_count += 1
            for j in b:
                if j in d:
                    b_count += 1
            return a_count == b_count
        
        return check(s[:n//2], s[n//2:])
        
