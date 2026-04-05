class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, currlist, total):
            if total == target:
                res.append(currlist.copy())
                return
            if i >= len(candidates) or total > target:
                return
            currlist.append(candidates[i])
            dfs(i+1, currlist, total + candidates[i])
            currlist.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            
            dfs(i+1, currlist,total)
        dfs(0,[],0)
        return res