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
        
        
