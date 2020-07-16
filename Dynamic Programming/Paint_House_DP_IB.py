#Paint House - Dp
def solve(arr):
    n = len(arr)
    # DP STATE
    # dp<Color>[i] = Minimum Cost of painting till ith House with 'Color'
    # Base Conditions = dp<Color>[0] = 0
    dpR = [0] * (n+1)
    dpG = [0] * (n+1)
    dpB = [0] * (n+1)
    #DP EXPRESSION
    # dp<Color>[i] = min(dp<other_colors>[i-1]) + Cost of this Color i.e arr[i][<color>]
    for i in range(1,n+1):
        dpR[i] = min(dpG[i-1], dpB[i-1]) + arr[i-1][0]
        dpG[i] = min(dpR[i-1], dpB[i-1]) + arr[i-1][1]
        dpB[i] = min(dpR[i-1], dpG[i-1]) + arr[i-1][2]

    #print(f'dpR: {dpR}')
    #print(f'dpG: {dpG}')
    #print(f'dpB: {dpB}')

    # Answer at min(dp<Color>[N]) - Minimum of all states to color till Nth Houses.
    return min(dpR[n], dpG[n], dpB[n])

print(solve([[1, 2, 3],[10, 11, 12],[4,5,9]]))

    
        
    
