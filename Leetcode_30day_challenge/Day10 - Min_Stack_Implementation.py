class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [[-1, 2147483647]]
        #To store the minimum number so far seen
        #self.min_stack = [2147483647]
        

    def push(self, x: int) -> None:
        self.stack.append([x,min(x,self.stack[-1][1])])


    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1] 


obj = MinStack()
obj.push(5)
obj.push(6)
obj.push(8)
print(obj.pop())
print(obj.top())
print(obj.getMin())
