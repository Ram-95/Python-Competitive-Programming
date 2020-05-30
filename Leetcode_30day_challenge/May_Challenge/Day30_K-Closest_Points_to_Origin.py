'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
'''

import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        dist = []
        def distance(loc):
            return sqrt(loc[0]**2 + loc[1]**2)
        
        for i in range(n):
            dist.append([distance(points[i]), i])
        
        dist.sort()
        ans = []
        
        for i in dist[:K]:
            ans.append(points[i[1]])
        
        return ans
        
        
