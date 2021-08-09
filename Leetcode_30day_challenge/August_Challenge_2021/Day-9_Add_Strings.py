"""
Time Complexity - O(max(len(num1), len(num2)))
Space Complexity - O(abs(len(num1) - len(num2)))
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        num1 = num1.rjust(n, '0')
        num2 = num2.rjust(n, '0')
        ans = ''
        carry = 0
        for i in range(len(num1)-1,-1,-1):
            temp = int(num1[i]) + int(num2[i]) + carry
            if temp > 9:
                carry = 1
            else:
                carry = 0

            ans = str(temp)[-1] + ans
        if carry > 0:
            ans = str(carry) + ans

        return ans
