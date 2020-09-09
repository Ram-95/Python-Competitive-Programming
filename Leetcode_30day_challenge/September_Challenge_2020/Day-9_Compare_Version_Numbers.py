class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Converting to List
        v1 = version1.split('.')
        v2 = version2.split('.')
        # Getting the maximum length
        n = max(len(v1), len(v2))
        
        # Extending the lists with Zeros so that both will be of same length
        v1 = v1 + [0] * (n - len(v1))
        v2 = v2 + [0] * (n - len(v2))
        
        version1, version2 = 0, 0
        
        # Converting the Version 1 to an Integer value
        idx = 0
        for i in reversed(v1):
            version1 += (10**idx) * int(i)
            idx += 1
        
        # Converting the Version 2 to an Integer value
        idx = 0
        for i in reversed(v2):
            version2 += (10**idx) * int(i)
            idx += 1
        
        # Conditions to return the answer
        if version1 > version2:
            return 1
        elif version1 < version2:
            return -1
        else:
            return 0
        
