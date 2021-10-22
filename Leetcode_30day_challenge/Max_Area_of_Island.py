# DFS Solution - O(M*N) Time and O(1) Space

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        def DFS(i, j, m):
            # Exit condition
            if i < 0 or j < 0 or i > rows-1 or j > cols-1 or m[i][j] == 0:
                return 0
            # Mark the current node as visited
            if m[i][j] == 1:
                m[i][j] = 0
            
                # N-4 Connectivity. Calling DFS on four neighbours
                x = DFS(i-1,j,m)
                y = DFS(i,j-1,m)
                z = DFS(i+1,j,m)
                t = DFS(i,j+1,m)
                
                sums = 1+x+y+z+t 
                
            return sums
        
        # Calling DFS for every set Node
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    curr = DFS(i,j,grid)
                    ans = max(ans, curr)
                
        return ans
