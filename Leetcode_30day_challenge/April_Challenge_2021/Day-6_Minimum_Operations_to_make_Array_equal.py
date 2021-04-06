# O(N) Time - Two Pointer technique
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
        
# O(1) Time - Formula Based
'''
Formula: We can infer that
1. If n is even, then answer is sum of all odd numbers till n/2. Say k = n/2, then sum of all odd numbers is k*k
2. If n is odd, then answer is sum of all even numbers till n/2. Say k = n/2, then sum of all even numbers is k*(k+1)
'''
class Solution:
    def minOperations(self, n: int) -> int:
        k = n // 2
        # if N is odd
        if n & 1:
            return k*(k+1)
        else:
            return k*k
        
        
