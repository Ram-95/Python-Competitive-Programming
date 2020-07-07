class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #Set to store the Indices of the Grids
        d = set()
        #Rows
        m = len(grid)
        #Columns
        n = len(grid[0])
        
        #Adding the indices of the grids to the set
        for i in range(m):
            for j in range(n):
                d.add((i,j))
        ans = 0
        
        #Main Logic
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    #Top grid of the current grid
                    if (i-1,j) not in d or grid[i-1][j] == 0:
                        ans += 1
                    #Left grid of the current grid
                    if (i,j-1) not in d or grid[i][j-1] == 0:
                        ans += 1
                    #Right grid of the current grid
                    if (i,j+1) not in d or grid[i][j+1] == 0:
                        ans += 1
                    #Bottom grid of the current grid
                    if (i+1,j) not in d or grid[i+1][j] == 0:
                        ans += 1
        
        return ans
                
        
