'''Method - 1 Using Inbuilt Function'''
class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        s = s[::-1].ljust(32, '0')
        return int(s, 2)


'''Method - 2 Bit Wise Operators'''
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n = n >> 1

        return ans
