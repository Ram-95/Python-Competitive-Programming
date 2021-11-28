"""
Use a dummy head, and

l, r : define reversing range

pre, cur : used in reversing, standard reverse linked linked list method

jump : used to connect last node in previous k-group to first node in following k-group
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node initialization
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head
        
        while True:
            count = 0
            # Moving k positions
            while r and count < k:
                count += 1
                r = r.next
            # If count == k, then reverse the segment [l, r]
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                # Joining the current k-group with the previous k-group
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next
