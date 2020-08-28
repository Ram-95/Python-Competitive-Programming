# Q: https://leetcode.com/problems/implement-rand10-using-rand7/submissions/
# Idea: rand7() -> rand49() -> rand40() -> rand10()

class Solution:
    def rand10(self):
        res = 40
        while res >= 40:
            # Generating random numbers from 1-49 ->  7 * (rand7() - 1)
            res = 7 * (rand7() - 1) + (rand7() - 1)
        # +1 to generate 10 as random number
        return res % 10 + 1
        
