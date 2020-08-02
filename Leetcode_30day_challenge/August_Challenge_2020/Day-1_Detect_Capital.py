class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.title() or word == word.upper() or word == word.lower():
            return True
        return False
