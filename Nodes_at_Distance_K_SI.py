#Nodes at Distance K from the given source node - Smart Interviews

from collections import deque

class Node:
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            t_root = self.root
            while True:
                if data < t_root.data:
                    if t_root.left:
                        t_root = t_root.left
                    else:
                        t_root.left = Node(data)
                        break
                elif data > t_root.data:
                    if t_root.right:
                        t_root = t_root.right
                    else:
                        t_root.right = Node(data)
                        break
                else:
                    break

    #Searches for a node whose value is 'val' and returns the Node
    def search(self, root, val):
        if root is None:
            return 0
        
        if root.data == val:
            return root
        if val < root.data:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)


def Preorder(root):
    if root is None:
        return
    #Adding the Nodes to the 'PRE' array
    pre.append(root)
    Preorder(root.left)
    Preorder(root.right)
    


#Driver Code
t = int(input())
while t:
    (n,s,k) = (map(int, input().rstrip().split()))
    arr = list(map(int, input().rstrip().split()))

    #Creating Tree and inserting the data
    tree = Tree()
    for i in range(n):
        tree.insert(arr[i])
    src_node = tree.search(tree.root, s)

    #Stores the Nodes in the order of Preorder
    pre = []

    #Dictionary to store the Parents {Child: Parent}
    d = {}

    #Root Node's Parent is -1
    d[tree.root] = -1

    #Preorder Traversal
    Preorder(tree.root)

    #Visited array to keep track of visited Nodes {Node: True or False}
    vst = {}
    
    #To populate the Parents Dictionary
    for i in pre:
        #Visited Hashmap used in BFT
        vst[i] = False
        if i.left is not None:
            d[i.left] = i
        if i.right is not None:
            d[i.right] = i


    #Queue for BFT
    q = deque()
    count = 0
        
    #Adding the source Node to the queue ; -1 acts as stopper i.e, end of level
    q.append(src_node)
    q.append(-1)

    #Marking the source node as visited
    vst[src_node] = True

    '''Main Logic | Breadth First Traversal(BFT) - Using -1 as separator'''
    while q and k:
        while True:
            temp = q.popleft()
            if temp == -1:
                break
            else:
                vst[temp] = True
                #Add the Parent Node
                if d[temp] != -1:
                    if vst[d[temp]] == False:
                        q.append(d[temp])
            
                #Add the left and right Nodes; if they exist.
                if temp.left is not None:
                    if vst[temp.left]  == False:
                        q.append(temp.left)

                if temp.right is not None:
                    if vst[temp.right] == False:
                        q.append(temp.right)
        
        #Append -1 to denote Completion of Adding all Neighbours of all adjacent Nodes.
        q.append(-1)
        k -= 1
    
    print(f'{len(q) - 1}')
        
    t = t - 1
