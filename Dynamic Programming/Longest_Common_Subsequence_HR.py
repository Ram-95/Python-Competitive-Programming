def longestCommonSubsequence(text1: str, text2: str) -> int:
    '''Prints the LCSS of the given two strings.'''
        text1.insert(0, '')
        text2.insert(0, '')
        
        n = len(text1)
        m = len(text2)
        
        #DP array
        dp = [[0 for i in range(m)] for j in range(n)]
 
        ans = []
        for i in range(1,n):
            for j in range(1,m):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
             
    
        def dp_ans(dp,i,j):
            if i <= 0 or j <= 0:
                return
            elif text1[i] == text2[j]:
                ans.append(text1[i])
                dp_ans(dp,i-1,j-1)
            else:
                if dp[i-1][j] >= dp[i][j-1]:
                    dp_ans(dp,i-1,j)
                else:
                    dp_ans(dp,i,j-1)
                
        dp_ans(dp, n-1, m-1)   
        ans = [int(x) for x in ans]
        print(*ans[::-1])


(n,m) = (map(int, input().split()))
t1 = list(map(str, input().split()))
t2 = list(map(str, input().split()))
longestCommonSubsequence(t1, t2)
