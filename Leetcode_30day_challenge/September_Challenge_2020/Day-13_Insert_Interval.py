'''
Method: 
1. Append the newInterval to the given intervals list
2. Sort the intervals list 
3. Merge the overlapping intervals in the intervals list
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        # Appending the newInterval to the intervals list
        intervals.append(newInterval)
        # Sorting the intervals list - Will take O(N) Time - Because Python uses Tim Sort internally
        intervals.sort()
        
        ''' Merging the intervals '''
        # Stack to compare the intervals and modify intervals
        st = [intervals[0]]
        for i in intervals[1:]:
            if i[0] in range(st[-1][0], st[-1][1]+1):
                st[-1][1] = max(i[1], st[-1][1])
            else:
                st.append(i)
            
        return st
