from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            # Calculate the area with the current pointers
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            
            # Move the pointer that points to the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
