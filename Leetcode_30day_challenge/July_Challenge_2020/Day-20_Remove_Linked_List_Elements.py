# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Base Case - When the LL is Empty
        if head is None:
            return None
        # To handle the case where the LL has all values as given 'val'
        while head:
            if head.val == val:
                head = head.next
                if head is None:
                    return None
            else:
                break
        
            
        # Temporary Head Pointer        
        t_head = head
        
        while t_head.next:
            if t_head.next.val == val:
                #print(f'Found after {t_head.val}')
                t_head.next = t_head.next.next
            else:
                t_head = t_head.next
        
        return head
            
        
