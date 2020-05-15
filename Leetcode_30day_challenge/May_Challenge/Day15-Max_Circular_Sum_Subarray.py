class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        flag = 0
        for i in A:
            if i > 0:
                flag = 1
                break
                
        if not flag:
            return max(A)
        
        def kadane(arr):
            ''''Kadane Max Sum Subarray Algorithm'''
            ans = arr[0]
            x = arr[0]
            
            for i in range(1,len(arr)):
                x = max(x,0) + arr[i]
                ans = max(ans, x)
            
            return ans
        
        #Case 1: When there is NO Wrap around, Finding max sum subarray in A
        c1 = kadane(A)
        #Case 2: When there is Wrap around, finding the max sum subarray by inverting the sign of elements in A and running Kadane on the modified Array.
        c2 = sum(A)
        
        #Inverting the signs
        A = [-x for x in A]
        
        #Adding the sum of original array and the max sum subarray of the modified array. By this we are effectively removing the elementa that do NOT contribute to the max sum subarray.
        c2 += kadane(A)
        
        #Return the maximum of two sums - cases 1 and 2
        return max(c1, c2)
