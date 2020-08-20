'''Q: https://leetcode.com/problems/reorder-list/'''
# My Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Base Conditions
        if head is None:
            return None
        elif head.next is None:
            return head
        
        def find_middle(head):
            '''Returns the middle node of LL.'''
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reverseLL(head):
            '''Reverse a LL.'''
            prev = None
            while head:
                x = head.next
                head.next = prev
                prev = head
                head = x
            return prev
        
        
        t_head = head
        middle_node = find_middle(t_head)
        
        # First half of LL
        l1 = head
        
        # Second half of LL
        l2 = middle_node.next
        middle_node.next = None

        l2 = reverseLL(l2)
        
        head_new = ListNode(0)
        temp = head_new
        
        while l1 and l2:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        
        # Appends the remaining Node if exists - Possible when the LL is Odd Length
        temp.next = l1 or l2
        
        return head_new



#--------------------------------------------------------------------------------------------------------#
# Method to Merge the Lists alternatively in-place
def _mergeLists(a, b):
            '''Merges the Two lists in place.'''
            tail = a
            head = a

            a = a.next
            while b:
                tail.next = b
                tail = tail.next
                b = b.next
                if a:
                    a, b = b, a

            return head
