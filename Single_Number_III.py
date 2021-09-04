"""
Time: O(N) and Space: O(1)

1. First pass: Find the XOR of those two numbers. let it be 'ans'
2. Find any position in ans where a bit is set.let it be 'pos'
3. Second pass: Divide the numbers into two groups(g1 and g2) based on - if that position 'pos' is set or not. This will make the two numbers fall in different groups.
4. Now again find the XOR of the individual groups and the result of the XOR will be the answer (those two digits)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #First pass - Do XOR and find the XOR of those two elements - will be stored in ans
        ans = 0
        for i in nums:
            ans ^= i
        
        # Find any random set bit position in ans
        def find_set_pos(n):
            for i in range(32):
                if n & (1 << i):
                    return i
        
        def check_bit_set_at_pos(m, k):
            return (m >> k) & 1
        
        pos = find_set_pos(ans)        
        res = [0, 0]
        for i in nums:
            if check_bit_set_at_pos(i, pos):
                res[0] ^= i
            else:
                res[1] ^= i
                
        return res
