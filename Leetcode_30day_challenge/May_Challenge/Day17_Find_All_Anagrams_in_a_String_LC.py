class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        n = len(s)
        m = len(p)
        
        if m == 0 or n == 0 or m > n:
            return ans
        
        #Count Array for the pattern 'p'
        count_p = [0] * 26
        for i in p:
            count_p[ord(i) - ord('a')] += 1
        
        def check(count_s, count_p):
            '''Returns True if both the count arrays are equal. '''
            for i in range(26):
                if count_s[i] != count_p[i]:
                    return False
            return True
        
        #Count Array for the String 's'
        count_s = [0] * 26
        #Window size - the size of pattern - Solved this problem using Sliding Window Concept
        window = m
        
        #Populating the Count array of the first window of the String
        for i in range(m):
            count_s[ord(s[i]) - ord('a')] += 1
        if check(count_s, count_p):
            ans.append(0)
        
        #Sliding the Window, Updating the Count array of String and checking if the current window and pattern are Anagrams.
        for i in range(m, n):
            #'prev' stores the item(The element left side of the current window) whose frequency should be decremented. 
            prev = i - window
            count_s[ord(s[prev]) - ord('a')] -= 1
            #Updating the frequency of the new element in the current window
            count_s[ord(s[i]) - ord('a')] += 1
            
            #Checking if the Current Window and Pattern are Anagrams
            if check(count_s, count_p):
                ans.append(i-window+1)
        
        return ans
