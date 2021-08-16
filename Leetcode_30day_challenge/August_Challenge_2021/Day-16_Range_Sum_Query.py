class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre = []
        prev = 0
        for i in self.nums:
            self.pre.append(prev + i)
            prev = self.pre[-1]
        

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.pre[right] - self.pre[left-1]
        return self.pre[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
