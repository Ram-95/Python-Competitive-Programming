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

    
''' Optimized Solution Two Passes - O(N) Time and O(1) Space. '''
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # arr stores the two nodes -> kth from last and kth from first
        arr = []
        t_head = head
        n = 0
        # Finding the length of the LL
        while head:
            n += 1
            head = head.next
        
        head = t_head
        x = 0
        while t_head:
            x += 1
            if x == n-k+1:
                arr.append(t_head)
            if x == k:
                arr.append(t_head)
            t_head = t_head.next
        
        # Swapping the values
        arr[0].val, arr[1].val = arr[1].val, arr[0].val
        
        return head
        
''' Optimized One Pass Solution - O(N) Time and O(1) Space. '''

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1, n2, p = None, None, head
        while p is not None:
            k -= 1
            n2 = None if n2 == None else n2.next
            if k == 0:
                n1 = p
                n2 = head
            p = p.next
        n1.val, n2.val = n2.val, n1.val
        return head
