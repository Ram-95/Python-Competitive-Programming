''' My Solution - O(N) Time and Space. '''

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = set(candyType)
        ans = len(candyType)//2
        
        return min(ans, len(s))
