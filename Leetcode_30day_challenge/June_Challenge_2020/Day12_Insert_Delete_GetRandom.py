'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
'''

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.d = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.arr.append(val)
            self.d[val] = len(self.arr) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            #knowing the index of element to be deleted
            idx = self.d[val]
            last = self.arr[-1]
            
            #Swapping the element to be deleted with the last element
            self.arr[idx], self.d[last] = last, idx
            
            #Removing the element from the list and dictionary
            self.arr.pop()
            self.d.pop(val, 0)
            
            return True
        return False
            
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[random.randint(0,len(self.arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
