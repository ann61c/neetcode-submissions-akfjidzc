class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): #需要+1 从1跳过
                if target - nums[i] == nums[j]:
                    return [i, j]
        