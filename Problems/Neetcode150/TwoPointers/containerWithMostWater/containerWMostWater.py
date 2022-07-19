class Solution:
    def maxArea(self, height) -> int:
        if len(height) == 2:
            return min(height[0], height[1])
        
        l, r = 0, len(height)-1
        ans = 0
        while l < r:
            maxHeight = min(height[l], height[r])
            ans = max(ans,(maxHeight) * (r-l))
            
            if maxHeight == height[l]:
                l += 1
            elif maxHeight == height[r]:
                r -= 1
                    
        return ans