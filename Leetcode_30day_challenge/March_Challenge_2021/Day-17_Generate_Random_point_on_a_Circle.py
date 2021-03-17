import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center
        

    def randPoint(self) -> List[float]:
        # Equation of Circle: (x**2) + (y**2) = (r**2). Every point of the circle should satisfy this equation.
        while True:
            a,b = random.uniform(self.x - self.r, self.x + self.r),random.uniform(self.y - self.r, self.y + self.r)
            # Checking if the point (a,b) lie on the circle.
            if (a - self.x)**2 + (b - self.y)**2 <= self.r**2:
                return [a,b]
