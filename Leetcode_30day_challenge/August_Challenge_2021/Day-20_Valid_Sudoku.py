# My Solution - O(N^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = 9, 9
        # Check the Rows
        for i in range(rows):
            s = set()
            for j in range(cols):
                if board[i][j] in s and board[i][j] != '.':
                    return False
                s.add(board[i][j])
        
        # Check the Cols
        for i in range(cols):
            s = set()
            for j in range(rows):
                if board[j][i] in s and board[j][i] != '.':
                    return False
                s.add(board[j][i])
        
        # Check the Submatrices
        for i in range(0,9,3):
            for j in range(9):
                if j%3 == 0:
                    ss = set()   
                for el in board[j][i:i+3]:
                    if el != '.' and el in ss:
                        return False
                    else:
                        ss.add(el)
        return True


# A Better approach
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                if (val,'r',row) in seen:
                    return False
                if (val,'c',col) in seen:
                    return False
                if (val,row//3,col//3) in seen:
                    return False
                seen[(val,'r',row)] =True
                seen[(val,'c',col)]=True
                seen[(val,row//3,col//3)]=True
        return True
