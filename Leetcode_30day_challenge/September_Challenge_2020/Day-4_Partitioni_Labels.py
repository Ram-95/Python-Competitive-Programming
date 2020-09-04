''' My Solution - O(N) Time and O(26) Space
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3448/discuss/828005/Python-O(N)-Dictionary-and-Set
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # Stores the frequency of the characters of S
        d = collections.Counter(S)
        ans = []
        # Stores the characters
        present = set()
        temp = ''
        
        def check(present, d):
            '''Checks if all the contents of 'present' set are exhausted. i.e frequency is Zero'''
            for i in present:
                if d[i] > 0:
                    return False
            return True
            
        for i in S:
            present.add(i)
            temp += i
            d[i] -= 1
            # Check if the frequency of contents of 'present' set is exhausted - If True, append the length of 
            # temp to ans and reset temp to ''
            if check(present, d):
                ans.append(len(temp))
                temp = ''
        
        return ans
  
