class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        #Sorting in ascending order based on the second value
        intervals.sort(key= lambda x: x[1])
        #print(intervals)
        ans = 0
        new = [[intervals[0][0], intervals[0][1]]]
        for i in intervals[1:]:
            if i[0] < new[-1][1]:
                ans += 1
            else:
                new.append(i)
                
        
        return ans
        
