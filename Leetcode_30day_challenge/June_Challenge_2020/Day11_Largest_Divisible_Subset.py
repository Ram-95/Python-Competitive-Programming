'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
Read this and Do again == source: https://www.geeksforgeeks.org/largest-divisible-subset-array/
'''

class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return []
        #Sorting the elements in ascending order
        arr.sort()
        ans = []

        div_count = [1 for i in range(n)]
        prev = [-1 for i in range(n)]
        maxm = 0

        for i in range(1,n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    if div_count[i] < div_count[j] + 1:
                        div_count[i] = div_count[j] + 1
                        prev[i] = j

            if div_count[maxm] < div_count[i]:
                maxm = i

        #Printing the answer
        idx = maxm
        while idx >= 0:
            ans.append(arr[idx])
            idx = prev[idx]
        ans.sort()
        return ans
        
