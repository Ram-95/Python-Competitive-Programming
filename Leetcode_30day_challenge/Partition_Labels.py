# Time: O(N) and Space: O(N)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        # Store the first and last index of each character.
        for i,v in enumerate(s):
            if v not in d:
                d[v] = [i,i]
            else:
                d[v][1] = i
        
    
        
        # Now the problem is same as merge intervals.
        temp = list(d.values())
        st = [temp[0]]
        for item in temp[1:]:
            top = st[-1]
            if item[0] <= top[1]:
                top[1] = max(top[1], item[1])
                
            else:
                st.append(item)
        
        # Calculating the answer       
        ans = [x[1]-x[0]+1 for x in st]
        return ans
