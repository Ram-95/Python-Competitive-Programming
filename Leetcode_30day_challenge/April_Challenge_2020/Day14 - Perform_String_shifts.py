class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        d = {0:0, 1:0}
        
        for i in shift:
            if i[0] == 0:
                d[0] += i[1]
            else:
                d[1] += i[1]
        
        if d[0] > d[1]:
            ans = [0, d[0]-d[1]]
        elif d[1] > d[0]:
            ans = [1, d[1]-d[0]]
        else: 
            return s
        
        #Left shifting 
        if ans[0] == 0:
            left_1 = s[0:ans[1]%len(s)]
            left_2 = s[ans[1]%len(s): ]
            
            return left_2 + left_1
        
        #Right Shifting
        elif ans[0] == 1:
            right_1 = s[0: len(s) -(ans[1]%len(s))]
            right_2 = s[len(s)-(ans[1]%len(s)): ]
            
            return right_2 + right_1
        
