''' My Solution - Using inbuilt Dictionary - NOT RECOMMENDED. '''
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.d[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.d.get(key, None) is None:
            return -1
        return self.d[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self.d.get(key, None) is not None:
            del self.d[key]
        

''' Will implement my own hash-function very soon...'''
