class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        s = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = [i]
            else:
                d[pattern[i]].append(i)
        
        st = str.split()
        
        for i,v in enumerate(st):
            if v not in s:
                s[v] = [i]
            else:
                s[v].append(i)
        
        #print(d.values())
        #print(s.values())
        
        return list(d.values()) == list(s.values())
