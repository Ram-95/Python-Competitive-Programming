'''My Solution - O(N) Time and Space.'''

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        d = {}
	# Putting the items of nums in dictionary with their frequencies
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # Iterating over the keys of dictionary
        for i in d.keys():
	    # Find out the numbers that differ from the current number by 1
            a,b = i-1, i+1
	    # Stores the current answer - Possible answer in the current iteration
            curr = 0
	    # Update 'curr' only if the dictionary has either 'a' or 'b' in it and their frequency is greater than 0
            if d.get(a, -1) > 0:
                curr += d[a] + d[i]
            elif d.get(b, -1) > 0:
                curr += d[b] + d[i]
	    # Update the maximum answer possible
            ans = max(ans, curr)
            
        return ans 
