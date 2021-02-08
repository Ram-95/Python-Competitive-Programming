# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

'''*************************************************************** My Implementation - Using extra Space ****************************************************************'''
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.l = []
        while iterator.hasNext():
            self.l.append(iterator.next())
        
        self.size = len(self.l)
        #print(self.l)
        self.curr = 0
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        e = self.l[self.curr]
        return e
        

    def next(self):
        """
        :rtype: int
        """
        e = self.l[self.curr]
        self.curr += 1
        return e
        

    def hasNext(self):
        """
        :rtype: bool
        """
        #self.curr += 1
        return self.size > self.curr
 

'''*************************************************** My Implementation - Without extra Space. ************************************************************'''
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.t = iterator
        self.val = self.t.next() if self.t.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.val
        

    def next(self):
        """
        :rtype: int
        """
        e = self.val
        self.val = self.t.next() if self.t.hasNext() else None
        return e
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.val is not None

    
 
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
