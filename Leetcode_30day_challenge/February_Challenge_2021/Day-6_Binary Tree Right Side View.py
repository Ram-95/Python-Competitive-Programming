''' My Solution - Using Deque (Level Order Traversal) | O(N) Time and Space. '''

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        level_order(root, ans)
        return ans

def level_order(root, ans):
    q = deque()
    q.append(root)
    sep = '$'
    q.append(sep)
    prev = None
    while q:
        t = q.popleft()
        if t != sep and t:
            q.append(t.left)
            q.append(t.right)
        elif t is None:
            continue
        else:
            q.append(sep)
        if prev and t == sep and t != prev:
            ans.append(prev.val)
        elif prev and t == prev and t == sep:
            break
        prev = t
