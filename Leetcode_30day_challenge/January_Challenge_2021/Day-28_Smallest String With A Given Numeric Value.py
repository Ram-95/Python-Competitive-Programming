''' My Solution - O(N) Time and O(26) Space'''

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        d = {}
        a = ord('a')
        # Filling the dictionary with {index: char}
        for i in range(a, a+26):
            d[i-96] = chr(i)
        
        # stores the answer
        ans = ''
        
        while n and k:
            # Only add 'z' to answer if k > 26 and 
            if k > 26 and k-26 >= n-1:
                ans += d[26]
                k -= 26
            else:
                # variable to store the no.of 'a''s to be appended to make the string lexicographically smaller
                char_a = n - 1
                k = k - char_a if k > char_a else char_a
                ans += d[k]
                break
            n -= 1
        
        # Appending char_a number of 'a'`s to the answer
        while char_a:
            ans += 'a'
            char_a -= 1
        
        #Reverse the answer and return
        return ans[::-1]
                
        
