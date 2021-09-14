# Time: O(N) | Space: O(N)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        d = set()
        p1, p2 = 0, len(s)-1

        for i in range(97, 123):
            x = chr(i)
            d.add(x)
            d.add(x.upper())

        while p1 < p2:        
            if s[p1] not in d:
                p1 += 1
            if s[p2] not in d:
                p2 -= 1
            if s[p1] in d and s[p2] in d:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
        
        return ''.join(s)
