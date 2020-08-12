# Method - Brute Force - Compute the Pascal Triangle till 33rd row and return the answer

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [[1],[1,1]]
        for i in range(32):
            temp = []
            for j in range(len(arr[-1])-1):
                temp.append(arr[-1][j] + arr[-1][j+1])
            temp.append(1)
            temp.insert(0,1)
           
            arr.append(temp)
        
        
        return arr[rowIndex]
        
        
# Method - Using nCr
# Given kth row consists of the kCr values (k - Given K value; r in [0:k+1]) 
# Calculate the nCr values and return the answer
# Python's in-built module that calculates nCr

from math import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []
        if rowIndex == 0:
            return [1]
        
        for i in range(rowIndex+1):
            arr.append(math.comb(rowIndex,i))
        
        return arr

    
# Using zip() function
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
