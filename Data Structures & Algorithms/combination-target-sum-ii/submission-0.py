class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        def dfs(index, path, total):
            # if index > len(candidates):
            #     return
            if total > target:
                return
            elif total == target:
                res.append(path.copy())
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, path, total + candidates[i])
                path.pop()
            
        dfs(0, path, 0)
        return res