# Time: O(N) and Space: O(1)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        a = ord('a')
        d = {chr(c): c - a  for c in range(a, a+26)}
        rd = {c - a: chr(c) for c in range(a, a+26)}
        for i in range(len(shifts)-2,-1,-1):
            shifts[i] += shifts[i+1]
        
        ans = ''
        for i in range(len(s)):
            ans += rd[(d[(s[i])] + shifts[i]) % 26]
                
        return ans
