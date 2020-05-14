#Trie Data structure
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:
    '''Creates a Trie Data Stucture.'''
    def __init__(self):
        self.root = TrieNode()

    def _charToIndex(self, ch):
    '''Helper Function to find the index of a character in the range [0,25].'''
        return ord(ch) - ord('a')

    def insert(self, key):
    '''Inserts a word/key into the Trie.'''    
        t_root = self.root
        length = len(key)
        for i in range(length):
            idx = self._charToIndex(key[i])

            if not t_root.children[idx]:
                t_root.children[idx] = TrieNode()
            t_root = t_root.children[idx]

        t_root.isEnd = True

    def search(self, key):
    '''Returns True is given word is present in the Trie, else returns False.'''
        t_root = self.root
        length = len(key)
        for i in range(length):
            idx = self._charToIndex(key[i])
            if not t_root.children[idx]:
                return False
            t_root = t_root.children[idx]

        return t_root != None and t_root.isEnd

    def startsWith(self, key):
    '''Returns True if given word is present as a prefix in the Trie, else returns False.'''
        t_root = self.root
        length = len(key)
        for i in range(length):
            idx = self._charToIndex(key[i])
            if not t_root.children[idx]:
                return False
            t_root = t_root.children[idx]

        return True
        

#Driver Code
keys = ['the', 'their', 'there', 'they', 'these', 'thesis', 'apple', 'appy', 'cat', 'catfish', 'cattle', 'cats']

#Creating a Trie Object
t = Trie()

#Inserting Keys into the Trie
for key in keys:
    t.insert(key)

