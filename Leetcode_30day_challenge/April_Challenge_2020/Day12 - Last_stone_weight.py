import heapq

class Solution:
    def lastStoneWeight(self, x: List[int]) -> int:
        x = [-1*i for i in x]
        #Creating a Max heap of x
        heapq.heapify(x)

        while len(x) > 1:
            a = -1 * heapq.heappop(x)
            b = -1 * heapq.heappop(x)
            c = -1 * (a-b)

            if c != 0:
                heapq.heappush(x,c)

        if len(x) == 1:
            return -1*x[0]
        elif len(x) == 0:
            return 0
        
