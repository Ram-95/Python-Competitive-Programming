'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #Pointers of Two, Three and Five
        (p2, p3, p5) = (0,0,0)
        #array to store the Ugly Numbers till 'n'.
        arr = [None] * n
        #First Ugly Number
        arr[0] = 1
        
        for i in range(1,n):
            #Assigning the minimum number of all the three values
            arr[i] = min(arr[p2]*2, arr[p3]*3, arr[p5]*5)
            
            #Incrementing the pointers of numbers, if the assigned value (min value) is same as the product
            if arr[i] == arr[p2] * 2:
                p2 += 1
            if arr[i] == arr[p3] * 3:
                p3 += 1
            if arr[i] == arr[p5] * 5:
                p5 += 1


        return arr[n-1]
       
