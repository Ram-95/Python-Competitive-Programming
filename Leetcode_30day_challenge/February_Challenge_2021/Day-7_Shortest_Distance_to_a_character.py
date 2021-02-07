class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        m = set()
        n = len(s)
        ans = []
        for i in range(n):
            if s[i] == c:
                m.add(i)
        #print(f'Set: {m}')
        for i in range(n):
            mn = float('inf')
            if s[i] == c:
                ans.append(0)
            else:
                for j in m:
                    mn = min(mn, abs(i-j))
                ans.append(mn)
                
        return ans
            
        
