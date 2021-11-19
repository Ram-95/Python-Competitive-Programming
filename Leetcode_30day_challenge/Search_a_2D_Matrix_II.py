# Solution - 1: For every row, apply Binary Search - Time: O(rows * log(cols))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        r,c = 0,0
        while r < rows and c < cols:
            start, end = matrix[r][0], matrix[r][-1]
            if target in range(start, end+1):
                low, high = 0, cols-1
                while low <= high:
                    mid = (low + high) // 2
                    if target == matrix[r][mid]:
                        return True
                    elif target < matrix[r][mid]:
                        high = mid-1
                    else:
                        low = mid+1
            r += 1
        return False


# Solution - 2: Start from the Top-right element and move the row and col pointer appropriately - Time: O(rows + cols)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        r,c = 0, cols-1
        """Idea: Start from top right element and keep applying Binary Search."""
        while r < rows and c >= 0:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        return False
