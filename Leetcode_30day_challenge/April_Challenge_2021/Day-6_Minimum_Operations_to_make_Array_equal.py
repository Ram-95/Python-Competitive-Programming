# O(N) Time
class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2*i)+1 for i in range(n)]
        target = sum(arr)//n
        ans = 0
        
        p1, p2 = 0, n-1
        
        while p1 < p2:
            ans += arr[p2] - target
            p2 -= 1
            p1 += 1
        
        
        return ans
        
