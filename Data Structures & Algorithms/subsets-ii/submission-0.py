class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = []
        nums.sort()
        def dfs(i, s):
            if i == len(nums):
                res.append(s.copy())
                return
            
            
            s.append(nums[i])
            dfs(i+1,s)
            s.pop()
            
            next_i = i+1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i +=1
            dfs(next_i,s)
            
        dfs(0, s)
        return res