#Is Subsequence - LeetCode
'''Time Complexity - O(s+t).'''

#Using Iterators
def isSubsequence(self, s, t):
    remainder_of_t = iter(t)
    for letter in s:
        if letter not in remainder_of_t:
            return False
    return True

#Two Pointer Approach
def solve(s, t):
    (m,n) = (len(s), len(t))
        
    #p1 - points to s; p2 - points to t
    (p1,p2) = (0,0)

    while p1 < m and p2 < n:
        if s[p1] == t[p2]:
            p1 += 1
            p2 += 1
        else:
            p2 += 1

    if p1 >= m:
        return True
    return False
    

s = 'afds'
t = 'fd'

print(solve(s, t))

