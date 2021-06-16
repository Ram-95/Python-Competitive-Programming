class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def solve(n, res, idx, op, cl, ans):
            if idx == n:
                ans.append(''.join(res))
                #print(res)
            if op < n//2:
                res[idx] = '('
                solve(n, res, idx+1, op+1, cl, ans)
            if cl < op:
                res[idx] = ')'
                solve(n, res, idx+1, op, cl+1, ans)
         
        arr = [None] * (2*n)
        
        solve(2*n, arr, 0, 0, 0, ans)
        return ans
