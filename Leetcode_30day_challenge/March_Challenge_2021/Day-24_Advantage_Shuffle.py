# My Solution - O(NlogN) Time & O(N) Space

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        A.sort()
        d = {}
        for i in sorted(B)[::-1]:
            if A[-1] > i:
                if i not in d:
                    d[i] = [A.pop()]
                else:
                    d[i].append(A.pop())
        
        #print(d)
        for i in B:
            if i in d and d[i] != []:
                ans.append(d[i].pop())
            else:
                ans.append(A.pop())
        
        return ans
        
            
    
        
