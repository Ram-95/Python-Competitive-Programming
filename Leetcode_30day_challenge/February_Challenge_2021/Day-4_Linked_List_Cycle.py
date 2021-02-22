'''My Solution - O(N) Time and Space'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        t_head = head
        while t_head:
            if t_head not in s:
                s.add(t_head)
            else:
                return True
            t_head = t_head.next
        
        return False

''' My Solution - O(N) Time and O(1) Space. - will be updated shortly'''
