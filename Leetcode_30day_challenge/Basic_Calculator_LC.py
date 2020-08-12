class Solution:
    def calculate(self, s: str) -> int:
        # Denotes if a parentheses is encountered
        op, cl = 0,0
        st = []
        num = ''
        post_fix = []
        for i in s:
            if i == ' ':
                continue
            elif i not in '()+-':
                num += i
                
            elif i in '()':
                if len(num) > 0:
                    post_fix.append(num)
                    num = ''
                if i == '(':
                    st.append('(')
                    op += 1
                else:
                    cl += 1
                    if op > 0:
                        while st and st[-1] != '(':
                            temp = st.pop()
                            post_fix.append(temp)
                        st.pop()
                        op -= 1
            elif i in '+-':
                if len(num) > 0:
                    post_fix.append(num)
                    num = ''
                while st and st[-1] in '+-':
                    temp = st.pop()
                    post_fix.append(temp)

                st.append(i)

        if num != '':
            post_fix.append(num)
        if st:
            while st:
                post_fix.append(st[-1])
                st.pop()
        


        # Evaluating Postfix
        st = []
        for i in post_fix:
            if i not in '+-':
                st.append(int(i))
            else:
                a = st.pop()
                b = st.pop()
                if i == '+':
                    ans = b + a
                else:
                    ans = b - a
                st.append(ans)

        return st[0]
        
