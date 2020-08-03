class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for i in s:
            if i.isalnum():
                temp += i.lower()
        #print(temp)
        return temp == temp[::-1]
        
