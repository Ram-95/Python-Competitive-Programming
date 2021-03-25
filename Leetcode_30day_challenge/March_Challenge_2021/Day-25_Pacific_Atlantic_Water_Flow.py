'''
Question explanation:
----------------------
The matrix is the continent with water on it and the boundaries are the oceans. Left and top being Pacific and right and bottom being the Atlantic.
The water on the continent (in the matrix) wants to flow out in the ocean. (Nature huh.)
The numbers in the matrix is the height of the water for that point.
For every point you have to ask the question. Can the water at this point and this height flow out in both the oceans under the constraints of flowing through only four(up, down, right, left) directions and flow into channels with same height or less height?
If yes you return the coordinate of that point. Else you ignore it.
To solidify this understanding, try to manually go to every point and see if the water can flow from there to both oceans or not.


BFS Solution

'''

from collections import deque
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        n = len(matrix)
        m = len(matrix[0])
        def BFS(ocean):
            q = deque(ocean)
            while q:
                (i,j) = q.popleft()
                for (di, dj) in [(0,1), (1,0), (-1,0), (0,-1)]:
                    row = di + i
                    col = dj + j
                    #print(f'Row: {row}\tCol: {col}')
                    if row in range(0,n) and col in range(0,m) and (row,col) not in ocean and matrix[row][col] >= matrix[i][j]:
                        q.append((row, col))
                        ocean.add((row, col))
            return ocean
        
        p = set([(i,0) for i in range(n)] + [(0,j) for j in range(m)])
        a = set([(n-1,i) for i in range(m)] + [(j, m-1) for j in range(n)])
        
        return list(BFS(p) & BFS(a))
        
