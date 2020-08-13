from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.comb = combinations(characters, combinationLength)
        #Calculates the length of the iterator
        self.size = sum(1 for _ in self.comb)
        #Recomputing the combination iterator as 
        #self.comb would be exhausted while calculating the size.
        self.comb = combinations(characters, combinationLength)
        

    def next(self) -> str:
        self.size -= 1
        return ''.join(next(self.comb))
        
    
        

    def hasNext(self) -> bool:
        return self.size > 0
    
        
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
