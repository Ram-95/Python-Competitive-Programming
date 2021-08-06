"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""

# Solution - 1
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Base Condition
        if root is None:
            return []
        
        q = deque()
        # Append the trees root
        q.append(root)
        # Separator - Separates Levels of the Tree
        sep = '$'
        # Append the separator - means end of root level
        q.append(sep)
        
        # Appending root.val to answer
        ans = [[root.val]]
        
        # Previous to check if all nodes are visited. Used to break while loop below
        prev = -1
        # A temporary list to store all nodes of each level
        temp = []
        while q:
            # Pop the first element of the deque
            curr = q.popleft()
            # If curr is not $, the we add it's children(the next level) one by one to the deque and temp list as well.
            if curr and curr != sep:
                for i in curr.children:
                    q.append(i)
                    temp.append(i.val)
            elif curr == sep:
                # if curr == $, that means we have reached the end of a level, so append temp list to answer.
                q.append(sep)
                if temp:
                    ans.append(list(temp))
                temp = []
            
            # Exit conditon. If curr == prev and they are both $,means we have completed traversing all levels
            if prev == curr and curr == sep:
                break
            
            # Updating the prev with curr
            prev = curr
            
                
        return ans
        

        
# Solution - 2 Pythonic Way
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Base Condition
        if root is None:
            return []
        # Append the root to deque
        q = deque([root])
        ans = []
        while q:
            # Append the list of nodes present in the deque
            ans.append([node.val for node in q])
            # Update/Append the Deque with the list of nodes from the next level.
            q = [node for nodes in q for node in nodes.children if node]
        
        return ans
