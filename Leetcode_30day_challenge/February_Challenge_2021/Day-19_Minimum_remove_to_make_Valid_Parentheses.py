class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                st.append([s[i], i])
            elif s[i] == ')':
                if st and st[-1][0] == '(':
                    st.pop()
                else:
                    st.append([s[i], i])

        while st:
            top = st.pop()
            s[top[1]] = ''
            
        return ''.join(s)
        
