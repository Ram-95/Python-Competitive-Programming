'''My Solution using deque.'''
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        ans = 0
        d = dict()
        q = deque()

        for i in s:
            if d.get(i,0) == 0:
                q.append(i)
                d[i] = 1
            else:
                while q and q[0] != i:
                    x = q.popleft()
                    d[x] -= 1
                q.popleft()
                q.append(i)
            ans = max(ans, len(q))

        return ans
        
        
'''Optimized solution of above. Instead of using a deque and popping elements one-by-one, we can directly calculate the answer.'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
