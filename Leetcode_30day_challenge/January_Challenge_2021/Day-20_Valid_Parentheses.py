class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        st = [-1]
        for i in range(n):
            if self.check(st[-1], s[i]):
                st.pop()
            else:
                st.append(s[i])
        if st == [-1]:
            return True
        return False
    
    def check(self, b1, b2):
        if b1 == '(' and b2== ')' or b1 == '[' and b2== ']' or b1 == '{' and b2== '}':
            return True
        return False
        
