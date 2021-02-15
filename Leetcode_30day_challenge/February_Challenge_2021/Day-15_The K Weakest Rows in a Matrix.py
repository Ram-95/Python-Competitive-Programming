''' My Solution - O(rows * cols) + O(rows) Time and O(rows) Space. '''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        rows, cols = len(mat), len(mat[0])
        
        for i in range(rows):
            d[i] = 0
            for j in range(cols):
                if mat[i][j] == 1:
                    d[i] += 1
        
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        return list(d.keys())[:k]
                
        
