''' My Solution - O(N) Time and O(1) Space. '''

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = 0
        temp = 0
        for i in range(len(S)):
            if S[i] == '(':
                temp += 1
            else:
                temp -= 1
            # If we encounter a (), then we increment ans by the 2th power of temp
            if S[i] == ')' and S[i-1] == '(':
                ans += 1 << temp
            
        return ans
