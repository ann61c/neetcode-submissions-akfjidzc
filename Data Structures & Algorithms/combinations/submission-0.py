class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(i, n, k, combination):
            if len(combination) == k:
                res.append(combination.copy())
                return
            if i > n:
                return

            combination.append(i)
            dfs(i+1, n, k, combination)
            combination.pop()
            dfs(i+1, n, k, combination)

        dfs(1, n, k, combination)
        return res