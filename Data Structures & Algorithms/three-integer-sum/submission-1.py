class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                break

            left = i + 1
            right = len(nums) - 1
            while left < right:
                output = nums[i] + nums[left] + nums[right]
                if output < 0:
                    left+=1
                elif output > 0:
                    right-=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    if left < right and nums[left] == nums[left - 1]:
                        left +=1
                    if left < right and nums[right] == nums[right + 1]:
                        right -=1

        return result
            
            