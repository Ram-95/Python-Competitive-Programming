#Trie Data structure
# '$' denotes the end of the word

class Trie:
    '''Creates a Trie Data Stucture.'''
    def __init__(self):
        self.Trie = {}


    def insert(self, key):
        '''Inserts a word/key into the Trie.'''
        t = self.Trie

        for i in key:
            if i not in t:
                t[i] = {}
            t = t[i]
        #Marking the end of the word
        t['$'] = '$'


    def search(self, key):
        '''Returns True is given word is present in the Trie, else returns False.'''
        t = self.Trie
        for i in key:
            if i not in t:
                return False
            t = t[i]
        if '$' in t:
            return True
        return False


    def startsWith(self, key):
        '''Returns True if given word is present as a prefix in the Trie, else returns False.'''
        t = self.Trie
        for i in key:
            if i not in t:
                return False
            t = t[i]
        return True
        

#Driver Code
keys = ['the', 'their', 'there', 'they', 'these', 'thesis', 'apple', 'appy', 'cat', 'catfish', 'cattle', 'cats']

#Creating a Trie Object
t = Trie()

#Inserting Keys into the Trie
for key in keys:
    t.insert(key)
