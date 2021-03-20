''' My Solution - DFS | O(E+V) Time '''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
      # Starting room
        start = [0]
      # To know if a room has been visited or not
        visited = set()
      # Adding the first room to set
        visited.add(0)
        while start:
            temp = start.pop()
            for i in rooms[temp]:
              # If a room is not visited, add it to the start and mark it as visited
                if i not in visited:
                    start.append(i)
                    visited.add(i)
        
        # If every room is visited return True else return False
        return len(visited) == len(rooms)

''' Minor Optimization '''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
      # Starting room
        start = [0]
      # To know if a room has been visited or not
        visited = set()
      # Adding the first room to set
        visited.add(0)
        while start:
            temp = start.pop()
            for i in rooms[temp]:
              # If a room is not visited, add it to the start and mark it as visited
                if i not in visited:
                    start.append(i)
                    visited.add(i)
            # Avoids unnecessary looping in some cases
            if len(visited) == len(rooms):
               return True
          
        return False
        
        
