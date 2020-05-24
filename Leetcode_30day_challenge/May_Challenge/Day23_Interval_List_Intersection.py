class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        n,m = len(A), len(B)
        
        while i < n and j < m:
            if A[i][1] < B[j][0]:
                i += 1
            elif B[j][1] < A[i][0]:
                j += 1
            else:
                ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] > B[j][1]:
                    j += 1
                else:
                    i += 1
        
        return ans
