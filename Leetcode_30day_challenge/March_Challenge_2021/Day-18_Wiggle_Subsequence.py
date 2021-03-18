''' My Solution - O(N) Time and O(1) Space. '''

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)   
        # Positive, Negative
        p, n = 1, 1

        for i in range(1,size):
            if nums[i-1] < nums[i]:
                p = n + 1
            elif nums[i-1] > nums[i]:
                n = p + 1
        
        #print(p,n)
        return max(p,n)
