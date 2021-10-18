# URL: https://leetcode.com/problems/remove-linked-list-elements/
# This method handles all the edge cases - All values are same, starting node value is val etc.,

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        t_head = dummy
        while t_head.next:
            if t_head.next.val == val:
                t_head.next = t_head.next.next
            else:
                t_head = t_head.next
        
        return dummy.next
     
