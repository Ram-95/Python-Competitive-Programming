'''Read this article: https://leetcode.com/problems/divide-two-integers/discuss/13407/C%2B%2B-bit-manipulations'''

#Division without using - *, -, / Operators

def div(dividend, divisor):
    INT_MIN = 	-2147483648
    INT_MAX = 2147483647

    #Base Condition
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    dvd = abs(dividend)
    dvs = abs(divisor)
    ans = 0

    sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
    while dvd >= dvs:
        temp = dvs
        m = 1
        while temp << 1 <= dvd:
            temp <<= 1
            m <<= 1

        dvd -= temp
        ans += m

    return sign * ans


