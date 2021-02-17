''' My Solution - O(N) Time and O(1) Space. '''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        
        # Pointers to Left and Right of heights list
        left, right = 0, n-1
        
        # Initial width - Width of whole heights list
        width = n-1
        
        while width > 0:
            area = max(area, width * (min(height[left], height[right])))
            
            # If left is greater than right height, decrease right pointer
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
            width -= 1
        
        return area
        
