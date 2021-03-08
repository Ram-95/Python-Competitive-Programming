''' My solution - O(N) Time and O(1) Space. '''
'''
Since there can be only two different characters in the string. The following cases are possible
1. If string is empty then return 0
2. If string is palindrome, then we need just 1 move
3. If string is not a palindrome, then we can remove 'a'/'b' in one move and remove the remaining 'a'/'b' in the next move. So max 2 moves.

'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        elif s == s[::-1]:
            return 1
        return 2
        
