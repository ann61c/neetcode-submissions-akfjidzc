class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0 
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        res = 0
        while left < right:
            if max_left < max_right:
                left+=1
                if max_left > height[left]:
                    res += max_left - height[left]
                else:
                    max_left = height[left]
            else:
                right -=1
                if max_right > height[right]:
                    res += max_right - height[right]
                else:
                    max_right = height[right]
        return res