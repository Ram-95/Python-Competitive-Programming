# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3429/

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        arr = S.split()
        
        for i in range(len(arr)):
            if arr[i][0].lower() not in vowels:
                arr[i] = arr[i][1:] + arr[i][0]
            arr[i] += 'ma'
            arr[i] += 'a' * (i+1)
            #arr[i] = ''.join(temp)
                    
        return ' '.join(arr)
