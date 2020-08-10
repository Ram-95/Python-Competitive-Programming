#Rotten Oranges - Smart Interviews
def solve(grid, n):
    # set to store the fresh oranges indices (value == 1)
    fresh = {(i,j) for i in range(n) for j in range(n) if grid[i][j] == 1}
    # set to store the rotten oranges indices (value == 2)
    rot = {(i,j) for i in range(n) for j in range(n) if grid[i][j] == 2}
    # Answer - The number of days to rot all the oranges
    count = 0
    # Directions array - Makes easier to move to Left, Right, Top and Bottom (N-4 neighbourhood)
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while fresh:
        # If 'rot' set is exhausted before 'fresh' set is exhausted, that means - There exists atleast 1 oranged that will
        # NEVER ROT
        if not rot:
            return -1
        # Adding the directions array to the items(indices) of the 'rot' set only if the resultant indices lead to a fresh orange.
        # Contains the all the cells indices that will 'rot'.
        rot = {(i+di, j+dj) for i,j in rot for di, dj in directions if (i+di, j+dj) in fresh}
        # Removing the rotten oranges' indices from the fresh set.
        fresh -= rot
        count += 1
    
    return count

# Test Cases
t = int(input())
while t:
    n = int(input())
    # List to store the input
    grid = []
    for _ in range(n):
        temp = list(input().strip())
        # Typecasting to int
        temp = [int(x) for x in temp]
        grid.append(temp)
    #print(grid)
    print(solve(grid,n))
    t -= 1
