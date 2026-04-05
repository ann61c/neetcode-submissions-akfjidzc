class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        left = 0
        right = len(nums) - 1
        while nums[right] <= target:
            if nums[left] + nums[right] == target:
                res.append(left)
                res.append(right)
                break
            elif nums[left] + nums[right] > target:
                right -=1
            else:
                left += 1
        return res
