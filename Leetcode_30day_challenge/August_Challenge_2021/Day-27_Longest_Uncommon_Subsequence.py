#######################
1. Sort the words in order of decreasing length of strings and count the number of each word in a hashmap and do
#######################


class Solution(object):
    def findLUSlength(self, strs): 
        def isSub(w1, w2, count):
            for i in w2:
                if i == w1[count]:
                    count += 1
                if count == len(w1): 
                    return True
            return count == len(w2)
        
        d = collections.Counter(strs)
        strs.sort(key = len, reverse = True)
        for i in range(len(strs)):
            if d[strs[i]] == 1:
                res = any(isSub(strs[i], strs[j], 0) for j in range(i))        
                if res == False: return len(strs[i])
        return -1
