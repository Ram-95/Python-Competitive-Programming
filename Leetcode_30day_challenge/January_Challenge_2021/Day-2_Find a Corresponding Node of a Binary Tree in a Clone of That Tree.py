'''My Solution | Time - O(N)'''

class Solution:
    ans = None
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.inorder(cloned, target)
        return self.ans

    def inorder(self, root, target):
        if root is None:
            return
        self.inorder(root.left, target)
        if root.val == target.val:
            self.ans = root
            #print(f'Found: {root}')
        self.inorder(root.right, target)
