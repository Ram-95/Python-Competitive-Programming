#Maximum Non-adjacent Subsequence Sum - Smart Interviews

def max_non_adjacent_subseq_sum(arr, n):
    if n == 1:
        return arr[0]

    #DP Table
    dp = [0]*(n)

    #Base Condition
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    #DP Expression
    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], arr[i])

    print(dp)
    return max(dp)
    
    


t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(max_non_adjacent_subseq_sum(arr, n))
    t = t-1
