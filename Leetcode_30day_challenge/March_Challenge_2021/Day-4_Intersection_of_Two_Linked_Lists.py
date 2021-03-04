''' My Solution - O(N+M) Time and O(N) Space '''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        t_head = headA
        while t_head:
            s.add(t_head)
            t_head = t_head.next
        
        while headB:
            if headB in s:
                return headB
            headB = headB.next
        
        return None
