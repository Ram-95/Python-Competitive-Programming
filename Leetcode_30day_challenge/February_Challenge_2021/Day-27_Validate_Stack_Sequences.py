'''My Solution - O(N) Time and Space.'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        if n == 0:
            return True
		# p1 - points to pushed list; p2 - points to popped list
        p1,p2 = 0,0
        st = []
        while p1 < n and p2 < n:
			# Push items to stack until the items of 'pushed[p1]' and 'popped[p2]' doesn't match
            if pushed[p1] != popped[p2]:
                st.append(pushed[p1])
                p1 += 1
            else:
                p1 += 1
                p2 += 1
			# Keep popping items from stack(st) if top of 'st' and popped[p2] are same
            while st and st[-1] == popped[p2]:
                st.pop()
                p2 += 1
        
		# Finally if 'st' is empty, then it's a VALID sequence else NOT VALID sequence
        return st == []
     
