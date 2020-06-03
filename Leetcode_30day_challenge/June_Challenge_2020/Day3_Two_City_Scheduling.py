class Solution:
    def twoCitySchedCost(self, arr: List[List[int]]) -> int:
        n = len(arr)
        
        ''' Maximising the savings. If savings are higher send them to A, then send the 
        rest of the people to B.'''
        
        #Array to store the index and the difference of the costs (B-A)
        res = [[x[0], x[1][1]-x[1][0]] for x in enumerate(arr)]

        #Sorting based on the difference(Savings) - Sorts based on the second value in Increasing Order. 
        res.sort(key=lambda x: -x[1])
        ans = 0

        for i in range(n):
            if i <= n//2 - 1:
                #Should go to A
                ans += arr[res[i][0]][0]
            else:
                #Should go to B
                ans += arr[res[i][0]][1]

        return ans
        
