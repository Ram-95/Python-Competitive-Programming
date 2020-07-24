# Link: https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Answer to store the paths
        ans = []
        # List to store the individual paths from each node
        temp = []
        # Appending the first Node of Graph
        temp.append(0)
        
        def solve(ans, graph, curr, temp):
            # If the current Node is the last node of the graph, then we've reached the End of that path.
            # So append the path in 'temp' to the 'ans' list.
            if curr == len(graph) - 1:
                ans.append(list(temp))
                return
            
            # Add every neighbour of the Current Node to the temp list and recur for the neighbour added
            for i in graph[curr]:
                temp.append(i)
                solve(ans, graph, i, temp)
                # After recurring for the newly added node, remove it from the temp list
                temp.pop()
        
        # Calling the solve method from the first node of the graph
        solve(ans, graph, 0, temp)
        
        # Returning the answer
        return ans
        
