class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        #DP State - dp[i][j] = minimum number of operations required to convert word1 of size 'i' 
        #to word2 of size 'j'.
        
        #Creating a DP Matrix
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        '''Base Conditions - The minimum no. of operations to convert string of length 0 to string of length greater than or equal to 0 and Vice Versa.'''
        #First Column
        for i in range(1,n+1):
            dp[i][0] = 1 + dp[i-1][0]
            
        #First Row
        for j in range(1,m+1):
            dp[0][j] = 1 + dp[0][j-1]
        
        '''Main Logic'''
        for i in range(1,n+1):
            for j in range(1,m+1):
                #If characters are matching -> We don't need to do anything. 
                #Answer is same as the diagonal i.e, subproblem dp[i-1][j-1].
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #If characters are not matching -> We can either Delete, Insert of Replace operations
                    #Since we need the minimum no. of operations - It is same as the 
                    #Minimum of answers of the Left, Top and Diagonal Cell + 1 
                    #i.e min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
        
        print(dp)      
        #Answer is at dp[n][m]
        return dp[n][m]
        
