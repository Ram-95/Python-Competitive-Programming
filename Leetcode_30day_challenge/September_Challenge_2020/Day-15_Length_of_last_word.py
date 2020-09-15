class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        
        return len(s.split()[-1])
       
