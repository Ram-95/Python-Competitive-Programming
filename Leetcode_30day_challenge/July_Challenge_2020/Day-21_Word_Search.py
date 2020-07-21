class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        #Rows
        m = len(board)
        #Columns
        n = len(board[0])
        
        def dfs(i,j,word):
            #print(f'Now: {word}')
            # If length of word is Zero that means the string is present in the board. Return TRUE
            if len(word) == 0:
                #print('Matched')
                return True
            # If the indices are valid - Call DFS on N-4 neighbours
            if (i < m and i >= 0) and (j < n and j >= 0):
                #print(i,j)            
                if board[i][j] == word[0]:
                    # Storing the matched value in temp. Used to restore later
                    temp = board[i][j]
                    
                    # Marking the visited character as '$'
                    board[i][j] = '$'
                    
                    # Calling DFS on all the four Neighbours
                    ans = dfs(i+1, j, word[1:]) or dfs(i-1, j, word[1:]) or dfs(i, j+1, word[1:]) or dfs(i, j-1, word[1:])
                    
                    # Restoring the character that is marked as visited - Because we may or may not find the answer in one direction. So we restore and this is Useful when Backtracking
                    board[i][j] = temp
                    
                    
                    return ans
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # If DFS returns True, return True - That is the word is Found
                    if dfs(i, j, word):
                        return True
        
        return False
                
        
            
