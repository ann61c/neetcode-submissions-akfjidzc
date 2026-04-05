class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        width = len(grid)
        height = len(grid[0])
        res = 0
        def dfs(i, j):
            if i < 0 or i >= width or j < 0 or j >= height:
                return 1
            if grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            if grid[i][j] == 1 and (i, j) not in visited:
                visited.add((i, j))
                return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        return dfs(0, 0)