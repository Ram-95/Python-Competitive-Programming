from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Using set to improve look up
        wordList = set(wordList)
        # Queue that contains the [word, length_so_far]
        queue = deque([[beginWord, 1]])
        
        # BFS Logic
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            # Replacing every position of 'word' with letters [a-z] and checking if the new word is present in the wordList
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    # If present, remove that word from the wordList set and add to the queue
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
