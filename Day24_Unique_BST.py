''' Given n - Number of Nodes. Return How may Unique BSTs can be constructed.'''
import math as m
class Solution:
    def numTrees(self, n: int) -> int:
        ans = (m.factorial(2*n)//(m.factorial(n)*m.factorial(n)))
        
        return ans//(n+1)
