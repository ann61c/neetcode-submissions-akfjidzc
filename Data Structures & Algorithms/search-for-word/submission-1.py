class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        width = len(board)
        height = len(board[0])
        #index, 
        # move through the board
 
        
        def dfs(word_i, i, j):
            if word_i == len(word):
                return True
            if i >= width or i < 0 or j >= height or j < 0:
                return False
            if board[i][j] == word[word_i]:
                original_char = board[i][j]
                board[i][j] = "#"
                res_bool = dfs(word_i + 1, i + 1, j) or dfs(word_i + 1, i - 1, j) or dfs(word_i + 1, i, j + 1) or dfs(word_i + 1, i, j - 1)
                board[i][j] = original_char
                return res_bool
            else:
                return False
        for w in range(width):
            for h in range(height):
                if dfs(0,w,h):
                    return True
        return False


            

