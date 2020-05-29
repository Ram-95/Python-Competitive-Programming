## This Problem is same as "Checking if a Directed Graph has Cycle or Not." using DFS.

'''
if node v has not been visited, then mark it as 0.
if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        #visited Array
        visited = [0] * numCourses
        
        #Creating a Directed Graph
        for i,j in prerequisites:
            graph[i].append(j)
            
        def DFS(v):
            if visited[v] == 1:
                return True
            elif visited[v] == -1:
                return False
            #If node 'v' is neither "visited" nor "being visited" then it is not "been visited" yet. So we mark it as "being visited" i.e, -1
            visited[v] = -1
            #Calling the DFS on the neighbours of current node.
            for nbr in graph[v]:
                if not DFS(nbr):
                    return False
            #Since we have visited the neighbours of the current node, we mark it as Explored i.e, 1
            visited[v] = 1
            
            return True
        
        #Calling DFS
        for node in range(numCourses):
            if not DFS(node):
                return False
        return True
