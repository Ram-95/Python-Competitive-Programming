# Time: O(N)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_LCA(root, p, q):
            if root.val < p.val and root.val < q.val:
                return find_LCA(root.right, p, q)
            elif root.val > p.val and root.val > q.val:
                return find_LCA(root.left, p, q)
            else:
                return root
        
        return find_LCA(root, p, q)
