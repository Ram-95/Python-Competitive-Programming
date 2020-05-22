class Solution:
    def frequencySort(self, s: str) -> str:
        #Since ASCII has 128 characters - We maintain an array of size 128. 'count' stores the [ASCII Code, frequency] of all the characters.
        count = [[i,0] for i in range(128)]
        ans = ''
        
        #Filling the Count array
        for i in s:
            count[ord(i)][1] += 1
        
        #Sorting the count array based on the second value of contents
        count.sort(reverse= True,key= lambda x: x[1])
        
        #Getting the answer by multiplying the string with its frequency and appending it to the answer.
        for i in count:
            ans += chr(i[0]) * i[1]
        
        return ans
        
