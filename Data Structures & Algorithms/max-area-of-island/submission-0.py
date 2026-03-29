class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        max_area = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            local_area = 0
            queue = collections.deque()
            visited.add((r, c))
            local_area += 1
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for cr, cc in directions:
                    nr = cr + row
                    nc = cc + col
                    if(nr in range(rows) and
                        nc in range (cols) and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visited):
                            visited.add((nr, nc))
                            local_area += 1
                            queue.append((nr, nc))
            return local_area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    local_area = bfs(r, c)
                    max_area = max(local_area, max_area)
        return max_area