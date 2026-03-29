class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        res = []
        p = []
        nums.sort()
        def dfs(p):
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                if len(p) == len(nums):
                    res.append(p.copy())
                    return
                if not visited[i]:
                    visited[i] = True
                    p.append(nums[i])

                    dfs(p)
                    
                    p.pop()
                    visited[i] = False
                
                
        dfs(p)
        return res