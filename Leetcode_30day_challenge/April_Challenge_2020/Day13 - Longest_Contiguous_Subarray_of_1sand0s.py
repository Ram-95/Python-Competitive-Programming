# Longest Contigous Subarray of equal number of 0's and 1's

class Solution:
    def findMaxLength(self, arr: List[int]) -> int:
        n = len(arr)
        d = {}
        pre_sum = 0
        ans = 0
        end_idx = -1
        
        for i in range(n):
            if arr[i] == 0:
                arr[i] = -1
            else:
                arr[i] = 1
        #print(arr)
        
        for i in range(n):
            pre_sum += arr[i]
            if pre_sum == 0:
                ans = i+1
                end_idx = i
                
            if pre_sum in d:
                if ans < i-d[pre_sum]:
                    ans = i - d[pre_sum]
                    end_idx = i
            else:
                d[pre_sum] = i
                
        return ans  
                
        
