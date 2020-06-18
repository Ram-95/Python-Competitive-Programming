class Solution:
    def hIndex(self, citations):
        if not citations: return 0
        n = len(citations)
        beg, end = 0, n - 1
        while beg <= end:
            mid = (beg + end)//2
            if mid + citations[mid] >= n:
                end = mid - 1
            else:
                beg = mid + 1                
        return n - beg
