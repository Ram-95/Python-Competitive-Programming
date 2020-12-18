class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sums_ab = []
        sums_cd = []
        n = len(A)
        
        # Calculating sum of lists A and B and storing the possible sum in sums_ab
        for i in range(n):
            for j in range(n):
                sums_ab.append(A[i] + B[j])
        
        # Calculating sum of lists C and D and storing the possible sum in sums_cd list
        for i in range(n):
            for j in range(n):
                sums_cd.append(C[i] + D[j])
        
        ans = 0
        # Dictionary to store the frequency of items in sums_cd
        d = {}
        for i in sums_cd:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        ### Now this part is same as Two Sum problem.
        # Given 'sums_ab' and 'sums_cd' lists. Find out the number of pairs whose sum is Zero.
        for i in sums_ab:
            if -i in d:
                ans += d[-i]
        
        return ans
