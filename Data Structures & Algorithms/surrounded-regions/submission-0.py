class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(board)
        cols = len(board[0])


        def dfs(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0 or board[r][c] == "X":
                return
            board[r][c] = "T"
            for dr, dc in directions:
                dfs(dr + r, dc +c)


        for r in range(rows):
            for c in range(cols):
                is_border = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
                if is_border and board[r][c] == "O":
                    dfs(r,c)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c]  = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


        