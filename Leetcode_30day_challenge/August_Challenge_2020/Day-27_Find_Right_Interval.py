'''
Q: https://leetcode.com/problems/find-right-interval/
'''

class Solution:
    def findRightInterval(self, arr: List[List[int]]) -> List[int]:
        def BS(lst, x):
            '''Binary Search to find the smallest value larger than x in lst and returns its index'''
            n = len(lst)
            low, high = 0, n-1
            idx = -1
            
            while low <= high:
                mid = (low + high)//2
                if lst[mid][0] >= x:
                    idx = lst[mid][1]
                    high = mid - 1
                elif lst[mid][0] < x:
                    low = mid + 1

            return idx
        
        
        n = len(arr)
        # Answer to store the indices
        ans = [-1 for _ in range(n)]
        # Creating a list that has the (first_values, index) of the lists in intervals
        f_val = [(v[0], i) for i,v in enumerate(arr)]
        # Creating a list that has the (second_values, index) of the lists in intervals
        s_val = [(v[1], i) for i,v in enumerate(arr)]    

        #Sorting both the lists on first values
        f_val.sort(key= lambda x: x[0])
        s_val.sort(key= lambda x: x[0])
        
        # For every value in s_val, we need to find the index of the smallest number that is larger than s_val.
        for i in s_val:
            # Calling Binary Search and storing the answer returned by BS
            ans[i[1]] = BS(f_val, i[0])
        
        # Return the answer
        return ans
