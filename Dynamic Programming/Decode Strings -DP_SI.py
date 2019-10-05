#Decode Strings - Dynamic Programming 

def decode_strings(s, n):
    '''dp[i] --> #Ways to decode a string'''
    #DP Table
    dp = [0]*(n+1)

    #Base conditions
    dp[0] = 1
    dp[1] = 1

    #DP Expression
    for i in range(2,n+1):
        #dp[i] = 0

        if s[i-1] >= '0':
            dp[i] = dp[i-1]

        if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '6'):
            dp[i] += dp[i-2]

    return dp[n]


t = int(input())
while t:
    n = int(input())
    s = input().lstrip().rstrip()
    print(decode_strings(s, n))
    t = t - 1
