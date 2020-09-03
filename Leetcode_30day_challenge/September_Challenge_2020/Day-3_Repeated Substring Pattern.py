class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp = (s+s)
        #Removing the first and the last character from temp
        temp = temp[1:-1]
        
        return temp.find(s) != -1
        
