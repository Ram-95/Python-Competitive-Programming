class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans_len = 0
        ans = ''
        d.sort(key=lambda x: (-len(x), x))
        print(d)
        for i in d:
            p1, p2 = 0, 0
            if len(s) >= len(i):
                while p1 < len(s) and p2 < len(i):
                    if s[p1] == i[p2]:
                        p1 += 1
                        p2 += 1
                    else:
                        p1 += 1
    
                if p2 == len(i):
                    return i
        
        return ans
