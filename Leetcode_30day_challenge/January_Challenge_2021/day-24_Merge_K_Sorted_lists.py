'''My Solution(Bruteforce) - O(NlogN) Time and O(N) Space.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []
        # Answer to store the final Linkedlist
        ans = ListNode()
        # Appending all the items of all the LL's into the nums list
        for i in lists:
            head = i
            while head:
                nums.append(head.val)
                head = head.next
        
        # Sorting the list
        nums.sort()
        # Storing the head of 'ans' LL
        head = ans
        # Inserting all the values of 'nums' list to 'ans' LL
        for i in nums:
            head.next = ListNode(i)
            head = head.next
        
        # Return the next of answer (bcoz the first node of ans will have 0 that we have inserted at the start.)
        return ans.next
