class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i >=1 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i+ 1
            right = len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum > target:
                    right-=1
                elif two_sum < target:
                    left+=1
                else:
                    res.append([nums[left], nums[i], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
        return res