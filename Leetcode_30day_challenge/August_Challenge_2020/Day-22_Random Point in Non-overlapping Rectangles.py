import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rectangles = rects
        self.sums = 0
        self.ranges = []
        for x1, y1, x2, y2 in self.rectangles:
            self.sums += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(self.sums)
    

    def pick(self) -> List[int]:
        x1, y1, x2, y2 = self.rectangles[bisect.bisect_left(self.ranges, random.randint(1, self.ranges[-1]))]
        return [random.randint(x1, x2), random.randint(y1, y2)]
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
