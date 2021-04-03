class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st, ans = [(")", -1)], 0
        n = len(s)
        
        for i in range(n):
            if s[i] == '(':
                st.append((s[i], i))
            else:
                if st[-1][0] == '(':
                    st.pop()
                    ans = max(ans, i-st[-1][1])
                else:
                    st.append((s[i],i))
        
        return ans
            
        
