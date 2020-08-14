'''
Q: Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        #print(d)
        arr = list(d.values())
        arr.sort(reverse=True)
        #print(arr)
        ans = 0
        '''
        Odd and Odd - Not possible (But the frequency - 1 will make a valid palindrome)
    
        Even and Odd - Possible
        Even and Even - Possible
        Odd and Even - Possbile
        
        '''
        for i in arr:
            if not(ans%2 == 1 and (i%2 == 1)):
                ans += i
            else:
                if i > 1:
                    ans += i-1
        
        return ans
                
                
            
            
        
