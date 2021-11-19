# Time:  O(N)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the intervals by the second value
        intervals.sort(key=lambda x: x[1])
        st = [intervals[0]]
        ans = 0
        for i in intervals[1:]:
            top = st[-1]
            if i[0] < top[1]:   # If there is an overlap, then that should't be considered
                ans += 1
            else:  
                # If there is no overlap, then that item should be considered. Add it to the stack
                st.append(i)
        
        return ans
