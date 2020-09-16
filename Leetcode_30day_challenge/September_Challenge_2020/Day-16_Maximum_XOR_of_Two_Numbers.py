# Maximum XOR of two numbers in Array

# Method - 1 - Brute Force | O(N^2) Time leads to TLE

# Method - 2 - Using Trie
class TrieNode():
    zero = None
    one = None
    value = None

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we'll first construct a tree that represents all the nums. 
        # The tree starts at `root` node, and all the leaf nodes in this tree will represent one num in nums.
        root = TrieNode()
        bit_range = range(31, -1, -1)       # [31, 30, .... 0]. We'll use this to iterate over num bit by bit.
        for num in nums:
            # always start at the top of the tree
            curr = root
            for i in bit_range:
                # get i'th bit in num
                mask = 1 << i               # mask will be something like 0000000100000, 1 being at the i'th position
                masked_num = num & mask     # if i'th bit was 0, masked_num is 0. Else masked_num is some number. In this case 100000 = 64
                if masked_num is 0:
                    # i'th bit was a 0, so traverse left (to zero), and create node as necessary
                    if not curr.zero:
                        curr.zero = TrieNode()
                    curr = curr.zero
                else:
                    # i'th bit was a 1, so traverse right (to one), and create node as necessary
                    if not curr.one:
                        curr.one = TrieNode()
                    curr = curr.one
            # Store num in the leaf node. 
            # We could always calculate it later ourselves by traversing the tree and using X*32+X*16+X*8+X*4+X*2+X*1 and so on
            # But I prefer this way, because it helps to point out that each leaf corresponds to a num in the nums array.
            curr.value = num

        # At this stage our tree is complete.
        # Note that, all the leaf nodes are at the same level - always 32. There are no leaf nodes in the tree that are at any level less or more than 32.
        # Also, note that the tree starts with the most significant bit (MSB) at the top, and least significant bit (LSB) at the bottom.

        # To calculate maximum overall xor, we'll first calculate maximum xor possible for each num in nums.
        # Side note: 1 xor 0 = 1; 0 xor 1 = 1; 1 xor 1 = 0; 0 xor 0 = 0
        # To calculate maximum possible xor value for num, we can traverse down the tree we constructed earlier.
        # How it works is, we'll go through bit-by-bit in num, from MSB to LSB.
        # If we're working with a 0, our goal is to find a 1. If we're working with a 1, our goal is to find a 0.
        # If we do find what we're looking for (our goal), Awesome! go there, then continue to next bit.
        # Otherwise, you gotta do something. So go to the remaining available node, and hope that the remaining bits in the number will give better results.
        # This greedy approach works, because even summing all the lower bits won't ever equal, even one bit higher. That is 10000 > 01111

        # Okay, let's go
        max_xor = 0
        for num in nums:
            curr = root
            for i in bit_range:
                # get i'th bit in num
                mask = 1 << i               # mask will be something like 0000000100000, 1 being at the i'th position
                masked_num = num & mask     # if i'th bit was 0, masked_num is 0. Else masked_num is some number. In this case 100000 = 64
                if masked_num is 0:
                    # i'th bit was a 0, so traverse right (to one)
                    if curr.one:
                        curr = curr.one
                    else:
                        # gotta do something
                        curr = curr.zero
                else:
                    # i'th bit was a 1, so traverse left (to zero)
                    if curr.zero:
                        curr = curr.zero
                    else:
                        # gotta do something
                        curr = curr.one
            # We are at a leaf node now. So we are at some value. 
            # This is the number that is most different from `num`. That is to say, will give the maximum possible XOR for num. 
            max_xor_for_num = num ^ curr.value
            #print(max_xor_for_num)
            if max_xor_for_num > max_xor:
                max_xor = max_xor_for_num

        return max_xor
