"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        #Corner Cases
        if head is None:
            return head
        
        
        #Stack to store the next Nodes of the Nodes that has a Valid Child Pointer i.e, Not None Child pointer
        st = []
        
        #Copying the head pointer to a temporary header so that we will not lose track of our DLL
        t_head = head
        
        while t_head:
            #If the child pointer of a Node is not none, then we append the next pointer of our current node
            #to the stack (only if the next node is not None).      
            if t_head.child is not None:
                if t_head.next:
                    st.append(t_head.next)
                #Making the Current Node and Child Node of the current node as adjacent Nodes
                t_head.next = t_head.child
                t_head.child.prev = t_head
                #Making the Child Node of current Node as 'None'
                t_head.child = None
            
            #Moving the head pointer to the next node.
            t_head = t_head.next
            
            #Using Temp to store the last Not None value of t_head
            if t_head:
                temp = t_head
         
        #Pop the nodes from the stack and make them the next nodes of the last node
        #Changing the next and prev pointers appropriately as it is a DLL
        while st:
            temp.next = st.pop()
            temp.next.prev = temp
            while temp.next:
                temp = temp.next
            
        
        #Return the Modified DLL Head Pointer
        return head
