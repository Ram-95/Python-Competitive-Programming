class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total_sequences = seq_count = 0

        for i in range(2, len(A)):
        	if A[i] - A[i-1] == A[i-1] - A[i-2]:
        		seq_count += 1
        		total_sequences += seq_count
        	else:
        		seq_count = 0

        return total_sequences
