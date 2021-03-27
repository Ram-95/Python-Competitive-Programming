''' Time - O(N^2) and O(1) Space. '''
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        # Base case
        if n == 0:
            return 0
        
        def solve(s, left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                # Extending the string from mid to the left. i.e, why Decrease left 
                left -= 1
                # Extending the string from mid to the right. i.e, why Increase right 
                right += 1
            return count
        
        for mid in range(n):
            # Finding the palindrome of Odd length strings
            ans += solve(s, mid, mid)
            
            # Finding the palindrome of Even length strings
            ans += solve(s, mid, mid + 1)
        
        return ans
        
