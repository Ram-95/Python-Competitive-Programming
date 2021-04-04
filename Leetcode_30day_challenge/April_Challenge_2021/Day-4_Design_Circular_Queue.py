from collections import deque

class MyCircularQueue:

    def __init__(self, k: int):
        self.d = deque(maxlen=k)
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if len(self.d) < self.k:
            self.d.append(value)
            return True
        return False
            
        
    def deQueue(self) -> bool:
        if len(self.d) > 0:
            self.d.popleft()
            return True
        return False
        

    def Front(self) -> int:
        if len(self.d) > 0:
            return self.d[0]
        return -1
        

    def Rear(self) -> int:
        if len(self.d) > 0:
            return self.d[-1]
        return -1
        

    def isEmpty(self) -> bool:
        return len(self.d) == 0
        

    def isFull(self) -> bool:
        return len(self.d) == self.k
        
