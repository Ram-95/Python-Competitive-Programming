'''My Solution - O(N * set size) Time and O(set size) Space.'''

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
            
'''
O(N) Solution using Min array of indices.
1. Traverse left to right and fill the array with difference of indices.
2. Traverse right to left and fill the array with difference of indices.
3. Ans is minimum indices of above.
'''     
