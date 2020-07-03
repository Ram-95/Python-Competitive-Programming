'''
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
'''

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        #The pattern keeps repeating after every 14 days
        MOD = 14
        ans = []
        for i in range(16):
            prev = list(cells)

            for j in range(1,7):
                if prev[j-1] == prev[j+1]:
                    cells[j] = 1
                else:
                    cells[j] = 0
            cells[0], cells[7] = 0, 0
            ans.append(list(cells))
        
        
        return ans[(N-1) % MOD]
