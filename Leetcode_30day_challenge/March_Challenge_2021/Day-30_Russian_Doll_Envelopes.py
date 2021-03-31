''' Refer this Explanation: https://leetcode.com/problems/russian-doll-envelopes/discuss/82751/O(Nlog(N))-python-solution-explained '''

class Solution(object):
    def maxEnvelopes(self, envs):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # sort first by increasing width
        # within each subarray of same-width envelopes
        # sort by decreasing height
        envs.sort(key=lambda w_h: (w_h[0],-w_h[1]))
        
        # now find the length of the longest increasing subsequence of heights.
        # Since each same-width block was sorted non-increasing, 
        # we can only pick at most one height within each block
        # otherwise, the sequence would be non-increasing
        tails=[]
        for (w,h) in envs:
            idx=bisect.bisect_left(tails, h)
            if idx==len(tails):
                tails.append(h)                        
            elif idx==0 or tails[idx-1]<h:
                tails[idx]=h
        return len(tails)
