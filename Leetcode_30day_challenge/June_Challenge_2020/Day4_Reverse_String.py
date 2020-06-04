#Reverse a string without using extra space. Do it Inplace.
#Used Two pointer approach.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        #Two pointer Approach
        (p1,p2) = (0,n-1)
        while p1 <= p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
