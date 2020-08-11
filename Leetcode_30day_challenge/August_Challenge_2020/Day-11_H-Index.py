class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse= True)
        ans = 0
        n = len(citations)
        for i,v in enumerate(citations):
            ans += i < v

        
        return ans
            
            
        
