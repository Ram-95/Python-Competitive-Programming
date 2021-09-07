class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            x = head.next
            head.next =  prev
            prev = head
            head = x
        
        return prev
