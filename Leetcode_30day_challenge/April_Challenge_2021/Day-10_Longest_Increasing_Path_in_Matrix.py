'''
To get max length of increasing sequences:
1. Do DFS from every cell
2. Compare every 4 direction and skip cells that are out of boundary or smaller
3. Get matrix max from every cell's max
4. Use matrix[x][y] <= matrix[i][j] so we don't need a visited[m][n] array
5. The key is to cache the distance because it's highly possible to revisit a cell
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # DP State:
        # dp(i,j) -> Denotes the length of Longest Increasing Path in a Matrix from (i,j) the element.
        
        # DP Matrix
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        ans = 1
        
        # DFS Traversal
        def DFS(matrix, i, j, rows, cols, dp):
            # If we already have a Longest path for (i,j) then we can return it
            if dp[i][j] != 0:
                return dp[i][j]
            res = 1
            # Traversing in all four directions of current element.
            for di, dj in [(-1,0), (1,0), (0,1), (0,-1)]:
                x,y = i+di, j+dj
                if x in range(rows) and y in range(cols) and matrix[x][y] > matrix[i][j]:
                    curr_len = 1 + DFS(matrix, x, y, rows, cols, dp)
                    res = max(res, curr_len)
            
            # Storing the answer in 'dp' matrix
            dp[i][j] = res
            
            return res
                    
        # For every element we traverse in all four directions and update the maximum answer
        for i in range(rows):
            for j in range(cols):
                x = DFS(matrix, i, j, rows, cols, dp)
                ans = max(ans, x)
        
        return ans
