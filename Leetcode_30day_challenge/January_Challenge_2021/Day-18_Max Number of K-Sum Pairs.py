'''My Solution: O(N) Time and O(N) Space.'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        ans = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        #print(d)
        for i in nums:
            diff = k-i
            if i != diff:
                if d.get(i,0) > 0 and d.get(diff,0) > 0:
                    ans += 1
                    d[i] -= 1
                    d[diff] -= 1
            else:
                if d.get(i,0) >= 2:
                    ans += 1
                    d[i] -= 1
                    d[diff] -= 1
                    
        #print(f'After: {d}')
        return ans
            
        
