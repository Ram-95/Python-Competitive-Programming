#Counting Duplicates
'''
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
'''

def countElements(arr):
        n = len(arr)
        count = 0
        d = {}
        
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in range(n):
            if arr[i] + 1 in d and d[arr[i]] > 0:
                count += 1
                d[arr[i]] -= 1
                
        return count

arr = [1,3,2,3,5,0]
print(countElements(arr))
