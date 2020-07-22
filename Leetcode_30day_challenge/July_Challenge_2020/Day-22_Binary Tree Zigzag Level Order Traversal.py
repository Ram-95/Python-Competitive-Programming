class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
	# A Dictionary that stores the {Depth: [Nodes at this Depth]}
        depths = {}
        def depth(root, d):
	''' Function to calculate depths of Nodes and saves them to the Dictionary''
            if root is None:
                return
            if d not in depths:
                depths[d] = [root.val]
            else:
                depths[d].append(root.val)
		# Recur for the Left Child Node. (d+1 because we are moving to the next depth)
            depth(root.left, d+1)
		# Recur for the Right Child Node. (d+1 because we are moving to the next depth)
            depth(root.right,d+1)
        
	# Calling Depth Function with the Root of the Tree. Since the depth of root node is 0, we pass 0 as depth
        depth(root, 0)
        
	# List to store our answer
        ans = []
	# A Flag to know when to reverse the nodes 
        even = 0
        for i in depths.values():
            if even%2 == 0:
			# If the even flag is 0, we append the list of node at this depth to our answer
                ans.append(i)
            else:
			# If the even flag is 1, then we reverse the list of nodes at this depth and append to our answer
                ans.append(list(i[::-1]))
            even += 1
        
        return ans
