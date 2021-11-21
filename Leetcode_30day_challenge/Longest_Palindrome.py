# Solution - 1 | Time: O(N) and Space: O(N)
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        
        for i in c.values():
            if ans % 2 == 1: # If odd
                if i % 2 == 0:  # If i is even, then it can be added
                    ans += i
                else:   # If i is odd, then (odd-1) which is even should be added
                    ans += i-1
            else:   #If even, either odd or even can be added.
                ans += i
        return ans
