class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        output = 0
        max_area = 0
        while left < right:
            output = (right - left) * min(heights[right], heights[left])
            max_area = max(max_area, output)
            if heights[left] < heights[right]:
                left+=1
            elif heights[left] > heights[right]:
                right-=1
            else:
                left+=1
                right-=1
            # output = max(output, (right - left) * min(heights[right], heights[left]))
        
        return max_area