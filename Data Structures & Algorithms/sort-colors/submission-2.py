class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        curr = 0 
        
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            
        while curr <= right:
            if nums[curr] == 0:
                swap(left, curr)
                left+= 1
                curr += 1
            elif nums[curr] == 2:
                swap(right, curr)
                right -=1
            curr += 1

            