'''
Solutions Based on the following fact: 
----------------------------------------
The even digits all have a unique letter while the odd digits all don't:

zero: Only digit with z
two: Only digit with w
four: Only digit with u
six: Only digit with x
eight: Only digit with g

The odd ones for easy looking, each one's letters all also appear in other digit words:
one, three, five, seven, nine

'''

''' Solution - 1 '''
class Solution:
    def originalDigits(self, s):
        d = collections.Counter(s)
        res = []
        for x in '0eroz 6six 7evens 5fiev 8eihtg 4ourf 3treeh 2tow 1neo 9nnei'.split():
            res.append(x[0] * d[x[-1]])
            for c in x:
                d[c] -= d[x[-1]]
        return ''.join(sorted(res))
        

''' Solution - 2 '''
class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        res += "0"*s.count('z')
        res += "1"*(s.count('o')-s.count('z')-s.count('w')-s.count('u'))
        res += "2"*s.count('w')
        res += "3"*(s.count('h') - s.count('g'))
        res += "4"*s.count('u')
        res += "5"*(s.count('f') - s.count('u'))
        res += "6"*s.count('x')
        res += "7"*(s.count('s')-s.count('x'))
        res += "8"*s.count("g")
        res += "9"*(s.count('i') - s.count('x') - s.count("g") - s.count('f') + s.count('u'))
        return res
