class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #Area covered by Hour hand
        deg_hour = (hour%12) * 30 + (minutes/2)
        
        #Area covered by minute hand
        deg_minutes = minutes * 6
        
        #Removing extra area that we included earlier
        total = abs(deg_hour - deg_minutes)
        
        #if total is lees than 180 return total, else return 360 - total
        return total if total < 180 else 360 - total
