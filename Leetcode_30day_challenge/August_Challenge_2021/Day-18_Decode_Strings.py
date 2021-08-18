class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1


        for i in range(2,n+1):
            if int(s[i-1:i]) in range(1,10):
                dp[i] += dp[i-1]
            if int(s[i-2:i]) in range(10,27):
                dp[i] += dp[i-2]

        
        return dp[n]
        
