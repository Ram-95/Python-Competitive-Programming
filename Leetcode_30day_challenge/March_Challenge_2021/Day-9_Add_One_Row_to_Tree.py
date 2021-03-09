''' My Solution - O(N) Time and Space.  '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, depth: int) -> TreeNode:
        # Dictionary to store the {depth: Nodes}
        depths = {}
        # Function that finds out the depth of a Node and updates 'depths' Dictionary
        def find_depth(root, d):
            if root is None:
                return
            if d not in depths:
                depths[d] = [root]
            else:
                depths[d].append(root)
            find_depth(root.left, d+1)
            find_depth(root.right, d+1)
        
        find_depth(root, 1)
        
        # Base Case - If d == 1
        if depth == 1:
            ans_root = TreeNode(v)
            ans_root.left = root
            return ans_root
        else:
            # For all the Nodes at "d-1" level, Make it's child Nodes as TreeNode(v) and
            # Point the actual children of the that Node to TreeNode(v).
            for i in depths[depth-1]:
                temp = i.left
                i.left = TreeNode(v)
                i.left.left = temp

                temp = i.right
                i.right = TreeNode(v)
                i.right.right = temp
        
        return root
