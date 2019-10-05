#Arranging Dominoes - Dynamic Programming Smart Interviews

def arranging_dominos(n):
    mod = int(1e9+7)
    if n == 1:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n >= 4:
        #DP Table
        dp = [None]*(n+1)

        #Base Conditions
        (dp[0], dp[1], dp[2], dp[3], dp[4]) = (1,1,2,3,5)
        
        
        #DP State
        '''dp[i] --> #Ways to fill a floor of size 5 X i'''

        #DP Expression
        for i in range(5,n+1):
            dp[i] = (dp[i-1] + dp[i-2])
            

        return dp[n] % mod
    


t = int(input())
while t:
    n = int(input())
    print(arranging_dominos(n))
    t = t - 1
