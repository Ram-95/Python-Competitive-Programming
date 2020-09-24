class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = collections.Counter(t)
        for i in s:
            d[i] -= 1
            if d[i] == 0:
                del d[i]
        #print(d.keys())
        
        return list(d.keys())[0]
        
