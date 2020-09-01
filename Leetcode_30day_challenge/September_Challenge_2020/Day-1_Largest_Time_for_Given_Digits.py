from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # Converting the elements to string
        A = [str(x) for x in A]
        # Generating the permutations of A
        s = permutations(A)        
        res = ""
        ans = -1
        
        for i in s:
            # Converting the i value to an integer
            temp = int(''.join(i))
            if temp < 2400 and ans < temp and int(''.join(i[2:])) < 60:
                ans = temp
                res = i
                # Converting to the required time format
                res = ''.join(res[:2]) + ':' + ''.join(res[2:])
        
        return res
