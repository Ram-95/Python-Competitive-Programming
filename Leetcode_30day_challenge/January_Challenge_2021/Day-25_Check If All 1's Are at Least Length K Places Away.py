''' My Solution - O(N) Time '''

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Get the position of first 1 in nums (if exists)
        # Else return is True (as No one's are present)
        if 1 in nums:
            pos = nums.index(1)
        else:
            return True
        
        # Iterate from post+1 to length of nums and update 'pos',
        # if you find any 1 with atleast 'k' distance from 'pos'.
        for i in range(pos+1, len(nums)):
            if nums[i] == 1:
                if abs(pos - i) < k+1:
                    return False
                else:
                    pos = i
        
        return True
                
                
        
