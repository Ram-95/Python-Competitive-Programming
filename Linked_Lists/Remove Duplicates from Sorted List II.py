# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head
        
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head.next = head.next.next
                head = head.next
                prev.next = head
            else:
                head = head.next
                prev = prev.next
        
        return dummy.next
