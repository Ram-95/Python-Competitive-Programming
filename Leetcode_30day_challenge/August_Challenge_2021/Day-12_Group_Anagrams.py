class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        sor = [''.join(sorted(list(x))) for x in strs]

        for i,v in enumerate(sor):
            if v not in d:
                d[v] = [strs[i]]
            else:
                d[v].append(strs[i])

        
        return (list(d.values()))
