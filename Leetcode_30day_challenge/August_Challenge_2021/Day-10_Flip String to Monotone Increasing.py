class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, flips = 0, 0
        for i in s:
            if i == '1':
                ones += 1
            else:
                flips += 1
            flips = min(flips, ones)
        
        return flips
        
