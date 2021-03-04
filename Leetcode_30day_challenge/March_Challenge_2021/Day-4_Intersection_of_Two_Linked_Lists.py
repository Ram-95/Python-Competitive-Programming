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
    

''' My Solution - O(N+M) Time and O(1) Space. '''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
            
        return p1
        
