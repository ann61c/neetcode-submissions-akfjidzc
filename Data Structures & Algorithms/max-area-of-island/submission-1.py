class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width = len(grid)
        height = len(grid[0])
        max_area = 0

        def dfs(i, j) -> int:
            area = 0
            if i >= width or j >= height or i < 0 or j < 0:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                area = 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return area

        for w in range(width):
            for h in range(height):
                if grid[w][h] == 1:
                    max_area = max(dfs(w, h), max_area)
        return max_area
