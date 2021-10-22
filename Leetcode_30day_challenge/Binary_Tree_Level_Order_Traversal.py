class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = [root]
        sep = '$'
        ans = []
        q.append(sep)
        res = []
        prev = -1
        while q:
            temp = q.pop(0)
            if prev == temp:
                break
            if temp != sep:
                res.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            else:
                ans.append(list(res))
                res = []
                q.append(sep)
            prev = temp
                
        return ans
