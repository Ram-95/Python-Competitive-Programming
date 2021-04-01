# O(N) Time and O(1) Space

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        sz = 0
        st = [float('inf')]
        t_head = head
        while t_head:
            t_head = t_head.next
            sz += 1
        
        t_head = head
        if sz % 2 == 0:
            while t_head:
                if t_head.val != st[-1]:
                    st.append(t_head.val)
                else:
                    st.pop()
                t_head = t_head.next
            
        else:
            temp = 0
            while t_head:
                temp += 1
                if temp == (sz//2) + 1:
                    t_head = t_head.next
                    continue
                if t_head.val != st[-1]:
                    st.append(t_head.val)
                else:
                    st.pop()
                t_head = t_head.next
            
        return st == [float('inf')]   
