# Two pointer Solution - O(N) Time and Space

# Method - 1
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res, start, end = [], 0, 1
        
        while end < len(S):
            if S[start] != S[end]:
                if end - start >= 3:
                    res.append([start, end-1])
                start = end
                end += 1
            else:
                end += 1
        
        # To handle the I/P like - 'aaa', 'aaabbb'
        if end - start >= 3:
            res.append([start, end-1])
        return res



# Method - 2
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res, start, end = [], 0, 1
        if len(S) <= 1:
            return res
        while True:
            if S[start] != S[end]:
                if end - start >= 3:
                    res.append([start, end-1])
                    
                start = end
                end += 1
            else:
                end += 1
            
            if end >= len(S):
                if end - start >= 3:
                    res.append([start, end-1])
                break
        
        return res
