class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefix_product = 1
        for i in range(len(nums)):
            res[i] = prefix_product
            prefix_product *= nums[i]
        suffix_product = 1
        for i in reversed(range(len(nums))):
            res[i] *= suffix_product
            suffix_product *= nums[i]
        return res 