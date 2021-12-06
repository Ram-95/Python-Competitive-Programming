# Solution - 1: Using List & Sort | Time: O(NlogN)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


# Solution - 2: Using Heap | Time: O(N) to build heap + O(KlogN) to find the Kth largest item
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # To put into Max Heap
        nums = [-x for x in nums]
        heapq.heapify(nums)
        while k:
            ans = heapq.heappop(nums)
            k -= 1
        
        return -ans
        

        
        
        
