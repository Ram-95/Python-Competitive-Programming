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
        
        
