'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
'''

class Solution:
    def calculateMinimumHP(self, arr: List[List[int]]) -> int:
        #rows
        m = len(arr)
        #cols
        n = len(arr[0])
        
        #Using DP from the right corner - Creating a DP Array with Max Value
        dp = [[1<<31 for i in range(n+1)] for j in range(m+1)]
        
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                ans = min(dp[i+1][j], dp[i][j+1]) - arr[i][j]
                dp[i][j] = 1 if ans <= 0 else ans

        return dp[0][0]
