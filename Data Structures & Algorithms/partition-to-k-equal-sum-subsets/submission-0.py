class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        if sum(nums) % k == 0:
            return True
        target = sum(nums) // k
        if max(nums) > target:
            return False
        
        res = []
        nums.sort()
        num = 0
        def dfs(i):
            if num == target:
                num.append(res)
                return
            if i > len(nums):
                return
            num += nums[i]
            dfs(i+1)
            num -= nums[i]
        dfs(0)
        return res