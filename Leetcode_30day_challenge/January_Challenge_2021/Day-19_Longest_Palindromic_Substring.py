class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            # Odd Length substring
            temp = self.helper(s, i, i)
            if len(temp) > len(ans):
                ans = temp
            
            # Even length substring
            temp = self.helper(s, i, i+1)
            if len(temp) > len(ans):
                ans = temp
            
        return ans
    
    # Helper function to grow the substring two ways until no more palindrome is found
    def helper(self, sub_str, left, right):
        while left >= 0 and right < len(sub_str) and sub_str[left] == sub_str[right]:
            left -= 1
            right += 1
        
        return sub_str[left+1:right]
        
