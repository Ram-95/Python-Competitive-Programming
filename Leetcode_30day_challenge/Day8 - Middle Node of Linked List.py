#Day8 - Middle node of Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        (p1, p2) = (head, head)
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
            
        
        return p1
