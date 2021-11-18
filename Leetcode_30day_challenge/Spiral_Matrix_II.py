class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:        
        mat = [[0  for _ in range(n)] for _ in range(n)]
        key = 1
        top, down, right, left = 0, n, n, 0
        
        # Directions - 0 -> left to right; 1 -> top to down; 
        # 2 -> right to left; 3 -> down to top
        d = 0
        while left <= right and top <= down:
            if d == 0:  # Move from Left to right
                for i in range(left, right):
                    mat[top][i] = key
                    key += 1
                top += 1
                d = 1
            elif d == 1:    # Move from Top to Down
                for i in range(top, down):
                    mat[i][right-1] = key
                    key += 1
                right -= 1
                d = 2
            elif d == 2:    # Move from right to left
                for i in range(right-1, left-1,-1):
                    mat[down-1][i] = key
                    key += 1
                down -= 1
                d = 3
            elif d == 3:    # Move from down to top
                for i in range(down-1, top-1, -1):
                    mat[i][left] = key
                    key += 1
                left += 1
                d = 0
        
        return mat
                
        
