#Minimum Cost Path - Dynamic Programming

'''
Given a maze with values, find the shortest path from first cell to the last cell. We can move in only Right and Down Directions only.
Also print the Path along with the cost.
'''
global path_list
path_list = []

def path(arr, i, j):
    ''' Prints the path that gives the Minimum Cost.'''
    if i < 0 or j < 0:
        return
    path_list.append(mat[i][j])
    (val, i, j) = (arr[i][j-1], i, j-1) if arr[i][j-1] < arr[i-1][j] else (arr[i-1][j], i-1, j)
    path(arr, i, j)
    


def solve(mat, n, m):
    dp = [[0  for i in range(m)]  for j in range(n)]

    #Base Conditions
    dp[0][0] = mat[0][0]

    #Marking the first row
    for i in range(1,m):
        dp[0][i] = dp[0][i-1] + mat[0][i]

    #Marking the first column
    for j in range(1,n):
        dp[j][0] = dp[j-1][0] + mat[j][0]

    #Dp Expression and State
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = mat[i][j] + min(dp[i][j-1], dp[i-1][j])
    print('\nDP Table:')
    for j in dp:
        print(*j)

    #Calling the path function to know the indices in the path taken.
    path(dp, n-1, m-1)

    return dp[n-1][m-1]

n,m = map(int, input().split())
mat = []

for _ in range(n):
    arr = list(map(int, input().split()))
    mat.append(arr)
print('Maze: ')
for i in mat:
    print(*i)
res = solve(mat,n,m)
print('\nCost: {}\nPath Taken: {}'.format(res, path_list[::-1]))


