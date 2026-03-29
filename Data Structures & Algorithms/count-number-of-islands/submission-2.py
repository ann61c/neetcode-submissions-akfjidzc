class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid)
        height = len(grid[0])
        islands = 0

        def dfs(i, j):
            if i >= width or j >= height or i < 0 or j < 0:
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        for w in range(width):
            for h in range(height):
                if grid[w][h] == "1":
                    islands += 1
                    dfs(w, h)
        return islands


