## Given a boolean array, find the Maximum subarray size
## that has equal no. of 1s and 0s.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        #Dictionary to store the index till which the sum is zero(equal no of 1s and 0s).
        d = {}
        sums = 0
        
        #Calculating sum and updating the answer if sum becomes zero.
        for i in range(n):
            #if element is 0 consider it as -1.
            if nums[i] == 0:
                sums += -1
            else:
                sums += nums[i]
            if sums == 0:
                #stores the length of subarray with equal 1s and 0s
                ans = i+1
                #stores the index of end of subarray whose sum == 0.
                end_idx = i
                
            if sums not in d:
                d[sums] = i
            else:
                ans = max(ans, i - d[sums])
              
        return ans
                
