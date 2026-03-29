class Solution:
    def trap(self, height: List[int]) -> int:
        # water_to_keep = 
        # min(left, tight) * distance of left and right

        # min(height[l], height[r]) - height[i]
        
        #for loop
        #left = 0
        #right = ?
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        water_trapped = [0] * len(height)
        prefix_max = 0
        suffix_max = 0
        for i in range(len(height)):
            prefix_max = max(prefix_max, height[i])
            prefix[i] = prefix_max

            suffix_max = max(suffix_max, height[len(height) - 1 - i])
            suffix[len(height) - 1 - i] = suffix_max
        
        for i in range(len(height)):
            water_trapped[i] = min(suffix[i], prefix[i]) - height[i]
        # print(water_trapped)
        return sum(water_trapped)
        
        
        

        # for i in range(len(height)):
        #     prefix_max.append(max(prefix_max[i], height[i]))
        # for i in range(len(height)):
        #     suffix_max[len(height) - i] = max(suffix_max[len(height) - i], height[i])
        # for i in height:
        #     water_trapped[i] = min(suffix_max, prefix_max) - height[i]
        # print(water_trapped)
