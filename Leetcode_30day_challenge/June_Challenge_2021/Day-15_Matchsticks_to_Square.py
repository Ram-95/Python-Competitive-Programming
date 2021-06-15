/*  */

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4
        sums = [0] * k
        subsum = sum(matchsticks)/k
        matchsticks.sort(reverse=True)
        
        def solve(i):
            if i == len(matchsticks):
                return len(set(sums)) == 1
            for j in range(k):
                sums[j] += matchsticks[i]
                if sums[j] <= subsum and solve(i+1):
                    return True
                sums[j] -= matchsticks[i]
                if sums[j] == 0:
                    break
            return False
        
        return solve(0)
