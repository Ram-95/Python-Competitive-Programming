class StockSpanner:

    def __init__(self):
        #Stack that stores the (element, index) of the element in the array
        self.st = []
    
    def next(self, price: int) -> int:
        count = 1
        while self.st and self.st[-1][0] <= price:
            count += self.st.pop()[1]
        self.st.append((price, count))
        
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
