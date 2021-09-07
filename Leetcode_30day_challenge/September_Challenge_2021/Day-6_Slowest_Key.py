class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans, max_val = keysPressed[0], releaseTimes[0]
        for i in range(1, len(keysPressed)):
            rtime = releaseTimes[i] - releaseTimes[i-1]
            
            if rtime > max_val:
                ans, max_val = keysPressed[i], max(max_val, rtime)
            elif rtime == max_val:
                ans = max(ans, keysPressed[i])
            
        return ans
        
