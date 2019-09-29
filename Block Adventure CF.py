def game(arr, n, m, k):
    i = 0
    ans = True
    for i in range(n-1):
        val = max(0, arr[i+1] - k)
        if val < arr[i]:
            m += arr[i] - val
        elif val - arr[i] > m:
            ans = False
            break
        else:
            m -= (val - arr[i])

    if ans:
        return 'YES'
    else:
        return 'NO'
 
        
        
    
 
t = int(input())
while t:
    nmk = list(map(int, input().rstrip().split()))
    n = nmk[0]
    m = nmk[1]
    k = nmk[2]
    #heights array
    arr = list(map(int, input().rstrip().split()))
    print(game(arr, n, m, k))
    t = t - 1
