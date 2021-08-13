class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        cr = set()
        cs = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    #matrix[i][0], matrix[0][j] = 0,0
                    cs.add(j)
                    cr.add(i)
                    
        for i in cr:
            matrix[i] = [0] * cols
        #print(matrix)
        for j in cs:
            for i in range(rows):
                matrix[i][j] = 0
                  
