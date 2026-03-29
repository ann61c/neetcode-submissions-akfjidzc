class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        p = []
        res = []

        def dfs(p):
            if len(p) == len(nums):
                res.append(p.copy())
                return
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    p.append(num)
                    dfs(p)
                    p.pop()
                    visited.remove(num)
        dfs(p)
        return res
    
        
            
