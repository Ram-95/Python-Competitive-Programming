# Solution - 1: O(N + M) Time and O(1) Space 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        t_head = dummy
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            t_head.next = ListNode(carry % 10)
            carry = carry//10
            t_head = t_head.next
        
        return dummy.next
            
