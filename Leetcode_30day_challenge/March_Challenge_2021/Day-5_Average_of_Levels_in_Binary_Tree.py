''' My Solution - BFS | O(N) Time and O(M) Space (M is the max. number of nodes in a level of the Tree.)'''

from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        d = deque()
        sep = '$'
        # Adding root node to the deque and separator after that
        d.append(root)
        # Separator denotes the end of current level
        d.append(sep)
        # Prev variable - Used in breaking loop
        prev = ''
        # Sum and Count of Nodes in current level
        sums, count = 0,0
        
        # BFS Code
        while d:
            top = d.popleft()
            # Condition to break - If you see two '$' back to back, then break from loop
            if prev == top and prev == sep:
                break
            if top != sep:
                sums += top.val
                count += 1
                # Adding the children of 'top' to the deque
                if top.left:
                    d.append(top.left)
                if top.right:
                    d.append(top.right)
            elif top == sep:
                ans.append(sums/count)
                sums, count = 0, 0
                d.append(sep)
            
            # Updating 'prev'
            prev = top
        
        return ans
