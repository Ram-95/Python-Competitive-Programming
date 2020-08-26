# HINT: This problem is Converting a base-26 number 
# to a base-10 Number.

# My Solution
class Solution:
    def titleToNumber(self, s: str) -> int:
        d = {}
        for i in range(65, 91):
            d[chr(i)] = i - 65 + 1
        n = len(s)
        #print(d)
        if n == 1:
            return d[s]
        ans = d[s[0]]
        for i in range(n-1):
            ans = ans * 26
            ans += d[s[i+1]]
            #print(ans)
            
        return ans
    
 

# Reverse of the above - Given Excel Column Number to Column Code
# Eg: I/P: 28 O/P: "AB"

# Excel Column Number to Column Code
def titleToNumber(n):
    d = {}
    ans = ''
    for i in range(65, 91):
        d[i - 65 + 1] = chr(i)
    #print(d)
    temp = []
    while n:
        quo, rem = divmod(n, 26)
        temp.insert(0,rem)
        n = quo if rem != 0 else quo - 1

    print(temp)
    for i in temp:
        if i != 0:
            ans += d[i]
        else:
            ans += d[26]

    return ans


n = int(input())
print(titleToNumber(n))



        
        
