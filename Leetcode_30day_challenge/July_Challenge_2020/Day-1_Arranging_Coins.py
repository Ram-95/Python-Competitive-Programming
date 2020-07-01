class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            mid = (low + high)//2
            temp = (mid*(mid+1))//2
            if temp == n:
                return mid
            elif temp > n:
                high = mid - 1
            else:
                low = mid + 1
                
        return high
