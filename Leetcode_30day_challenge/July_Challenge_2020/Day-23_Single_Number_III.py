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
        

'''
Method 2 - Concept - O(N) Time and O(1) Space
 
 - Let a and b be the two unique numbers
- XORing all numbers gets you (a xor b)
- (a xor b) must be non-zero otherwise they are equal
- If bit_i in (a xor b) is 1, bit_i at a and b are different.
- Find bit_i using the low bit formula m & -m
- Partition the numbers into two groups: one group with bit_i == 1 and the other group with bit_i == 0.
- a is in one group and b is in the other.
- a is the only single number in its group.
- b is also the only single number in its group.
- XORing all numbers in a's group to get a
- XORing all numbers in b's group to get b
- Alternatively, XOR (a xor b) with a gets you b.
'''
