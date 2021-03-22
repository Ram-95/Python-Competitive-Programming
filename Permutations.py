# This is the Optimized solution to generate the Permutations
''' Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order. '''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(arr, size):
            if size == 1:
                ans.append(list(arr))
                #print(arr)
                return 
            
            for i in range(size):
                solve(arr, size-1)
                
                # If size is odd, swap 0th and (size-1)th values
                if size & 1:
                    arr[0], arr[size-1] = arr[size-1], arr[0]
                else:
                    # If size is even, swap ith and (size-1)th values
                    arr[i], arr[size-1] = arr[size-1], arr[i]
        
        solve(nums,len(nums))
        return ans
                
        
