''' Linear Search - O(Rows * Cols) Time '''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target:
                    return True
        return False

    
''' Linear Search & Binary Search - O(Rows + log(Cols))''' 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            if target in range(matrix[i][0], matrix[i][-1]+1):
                row = matrix[i]
                #Binary Search Code
                low, high = 0, cols-1
                while low <= high:
                    mid = (low + high)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
        
        return False

    
''' Binary Search - O(log(Rows*Cols)) Time'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols-1
        while row >= 0 and row <rows and col>=0 and col <cols:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False
        
