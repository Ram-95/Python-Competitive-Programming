# Q: https://leetcode.com/problems/implement-rand10-using-rand7/submissions/
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        res = 40
        while res >= 40:
            # Generating random numbers from 1-42 ->  7 * (rand7() - 1)
            res = 7 * (rand7() - 1) + (rand7() - 1)
        # +1 to generate 10 as random number
        return res % 10 + 1
        
