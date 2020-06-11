#Top View of a Binary Tree - HackerRank

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    from collections import deque
    q = deque()
    q.append([root,0])
    #Dictionary to store the {Horizontal Distance: First Node that has this distance}
    s = {}
    
    #Breadth First Traversal - [To know the first node on either sides visited by Root]
    while q:
        temp = q.popleft()
        #Horizontal Distance from Root
        d = temp[1]
        #Adding the Left Child to the Queue (if Exists)
        if temp[0].left is not None:
            q.append([temp[0].left, d-1])
        #Adding the Right Child to the Queue (if Exists)
        if temp[0].right is not None:
            q.append([temp[0].right, d+1])
        #Adding the Horizontal Distance and the First Node that has this distance to Dict
        if d not in s:
            s[d] = temp[0].info
    
    #Printing out the Top View of Tree based on the values in the Dictionary.
    for i in sorted(s):
        print(s[i], end=" ")



#Driver Code
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
