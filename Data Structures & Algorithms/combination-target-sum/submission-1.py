class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        if sum(nums) == target:
            return nums

        def dfs(i, path, total):
            if i >= len(nums):
                return 
            if total == target:
                res.append(path.copy())
                return
            elif total < target:
                path.append(nums[i])
                dfs(i, path, total + nums[i])
                path.pop()
                dfs(i + 1, path, total)
            elif total > target:
                return
        dfs(0, path, 0)
        return res