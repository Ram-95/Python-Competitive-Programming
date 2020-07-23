''' 
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
'''

'''Method - 1 Using HashMap O(N) - Time and Space'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] -= 1
                # If the frequeny is 0,means we have seen the number twice. Delete such numbers from Dictionary
                if d[i] == 0:
                    del d[i]
        # Finally return the keys of the Dictionary
        return d.keys()
        
