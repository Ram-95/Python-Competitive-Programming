#Maximum Subarray Sum - Kadane Algorithm (Dynamic Programming)

def kadane_algo(arr, n):
    pre = []
    pre.append(arr[0])

    #Creating the Prefix sum array
    for i in range(1,n):
        pre.append(max(pre[i-1],0) + arr[i])

    #Maximum Sum of subarray
    val = max(pre)
    
    
    #Indices of the subarray whose sum is Maximum
    idx2 = pre.index(val)
    idx1 = 0
    
    #Finding out the starting index - idx1
    for i in range(idx2-1,-1,-1):
        if pre[i] < 0 and pre[i] != pre[i+1]:
            idx1 = i + 1
            break

    #Temporary Indices
    t_idx1 = idx1
    t_idx2 = idx2
    
    

    #Code for finding the lexicographically smallest subarray whose sum is Maximum   
    while (t_idx2 < n-1) and (t_idx1 <= t_idx2) and (val in pre[t_idx2+1:]):
            t_idx2 = pre[t_idx2+1:].index(val) + (t_idx2 + 1)
            #print(t_idx2)
            for i in range(t_idx2, t_idx1-1,-1):
                    if pre[i] < 0 and pre[i] != pre[i-1]:
                            t_idx1 = i + 1
                            break
            if idx2 - idx1 > t_idx2 - t_idx1:
                    (idx1, idx2) = (t_idx1, t_idx2)
        
            
    
    print('{} {} {}'.format(val, idx1, idx2))
    return
        

t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    kadane_algo(arr, n)
    t = t - 1
