class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]
        
        
        # rob1 = 0
        # rob2 = 0
        # for num in nums:
        #     temp = max(num + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = temp
        # return rob2

        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(nums[i] + dfs(i+2), dfs(i+1))
        # return dfs(0)