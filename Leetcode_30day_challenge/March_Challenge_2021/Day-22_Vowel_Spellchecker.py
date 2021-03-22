class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        if len(queries) == 0:
            return []
        
		# Set for Perfect Word
        wordPerfect = set(wordlist)
		# Dictionary to hold Capital Word Form
        wordUpper = {}
		# Dictionary to hold Vowel Chnaged Form
        wordVowel = {}
        
		# Setting up the Dictionaries and saving only the first correct occurance of the word in wordList
        for word in wordlist:
            tempLowerWord = word.lower()
            if tempLowerWord not in wordUpper:
                wordUpper[tempLowerWord] = word
			# Converting to Vowel Transformed Word
            tempWordVowel = self.changeVowelWord(tempLowerWord)
            if tempWordVowel not in wordVowel:
                wordVowel[tempWordVowel] = word
        
        ans = []
        for word in queries:
            tempWord = word.lower()
            tempWordVowel = self.changeVowelWord(tempWord)
			# If-Else priority wise, Capital before Vowel Transformed
            if word in wordPerfect:
                ans.append(word)
            elif tempWord in wordUpper:
                ans.append(wordUpper[tempWord])
            elif tempWordVowel in wordVowel:
                ans.append(wordVowel[tempWordVowel])
            else:
                ans.append("")
        
        return ans
        
    def changeVowelWord(self, word):
        
        myWord = ""
        for ch in word:
            if ch in "aeiou":
                myWord += '*'
            else:
                myWord += ch
        
        return myWord
