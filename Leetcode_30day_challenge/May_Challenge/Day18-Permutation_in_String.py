class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        a = ord('a')
        (m,n) = (len(s1), len(s2))
        
        if m > n:
            return False
        
        def check(c1, c2):
            for i in range(26):
                if c1[i] != c2[i]:
                    return False
            return True
        
        for i in s1:
            count1[ord(i) - a] += 1
            
        window = len(s1)
        
        for j in range(window):
            count2[ord(s2[j]) - a] += 1
    
        if check(count1, count2):
            return True
       
        #Sliding Window - Window is of size equal to length of s1
        for i in range(window,len(s2)):
            prev = i - window
            count2[ord(s2[prev]) - a] -= 1
            count2[ord(s2[i]) - a] += 1
            
            if check(count1, count2):
                return True
            
        return False
