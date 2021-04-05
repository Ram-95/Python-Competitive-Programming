class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        # DP STATE
        # dp(i) -> Longest string chain possible till ith element in words array.
        dp = {}
        
        for word in words:
            dp[word] = 1
            # Generate all the strings of length == len(word) - 1
            for i in range(len(word)):
                curr_str = word[:i] + word[i+1:]
                # If the generated string is in dp, 
                # then dp[word] = max(dp[curr_str] + 1, dp[word])
                if curr_str in dp:
                    dp[word] = max(dp[curr_str] + 1, dp[word])
            
        return max(dp.values())
