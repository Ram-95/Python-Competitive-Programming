'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        ans = []
        d = deque()
        #Separator of Levels
        sep = 's'
        #Adding the root node to the deque
        d.append(root)
        d.append(sep)
        idx = 0
        while idx < len(d):
            #Appending the Children of front node
            if d[idx] != sep:
                if d[idx].left:
                    d.append(d[idx].left)
                if d[idx].right:
                    d.append(d[idx].right)
                
            elif d[idx] == sep:
                #print(f'Appended after {d[idx-1].val}')
                d.append(sep)
               
            idx += 1
            prev = idx - 1
            #If previous and current item in Deque is same, that means the traversal is complete
            if d[prev] == d[idx]:
                break
        
        temp = []
        for i in d:
            if i != sep:
                temp.append(i.val)
            else:
                if temp:
                    ans.append(list(temp))
                temp.clear()
        
        return ans[::-1]                
        
