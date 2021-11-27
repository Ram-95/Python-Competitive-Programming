# Solution - 1: Swapping the Nodes (Iterative) | Time: O(N) and Space: O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base condition
        if not head or not head.next:
            return head
        t_head = head.next
        p1, p2 = head, head.next
        prev_p1 = None
        while p1 and p2:
            temp = p2
            p1.next = temp.next
            temp.next = p1
            
            if prev_p1:
                prev_p1.next = p2
            prev_p1 = p1    
            
            p1 = p1.next
            if p1:
                p2 = p1.next
            
        return t_head

# Solution - 1 Swapping the Nodes (Recursive) | Time: O(N) and Space: O(N)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head
            return temp
        
        return head
    

    # Solution - 2: Swapping the Values | Time: O(N) and Space: O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1, p2 = head, head.next
        t_head = head
        
        while p1 and p2:
            temp = p2.val
            p2.val = p1.val
            p1.val = temp
            
            if p2.next and p2.next.next:
                p1 = p2.next
                p2 = p1.next
            else:
                break

        return head
