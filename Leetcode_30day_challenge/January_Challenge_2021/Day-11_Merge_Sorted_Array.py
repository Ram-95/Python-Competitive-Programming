'''My - O(NlogN) Solution using Sort.'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sz = len(nums1) - m
        while sz:
            nums1.pop()
            sz -= 1
        
        nums1 += nums2
        nums1.sort()
