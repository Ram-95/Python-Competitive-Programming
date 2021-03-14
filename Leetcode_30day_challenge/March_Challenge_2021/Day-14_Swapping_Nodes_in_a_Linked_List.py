''' My Solution - 1 | O(N) Time and Space. '''

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        
        n = len(arr)
        arr[k-1], arr[n-k] = arr[n-k], arr[k-1]
        head = ListNode(arr[0])
        t_head = head
        for i in range(1, n):
            t_head.next = ListNode(arr[i])
            t_head = t_head.next
        
        return head

      
''' Slightly Optimized Solution - 2 | O(N) Time and Space.'''
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        arr = []
        t_head = head
        while head:
            arr.append(head)
            head = head.next
        
        n = len(arr)
        arr[k-1].val, arr[n-k].val = arr[n-k].val, arr[k-1].val
        
        return t_head
