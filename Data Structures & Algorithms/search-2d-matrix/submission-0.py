class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        row_to_search = -1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][-1] < target:
                top = mid_row + 1
            elif matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                row_to_search = mid_row
                break
        if row_to_search == -1:
            return False
        left = 0 
        right = len(matrix[row_to_search]) - 1
        

        while left <= right:
            mid_col = (left + right) // 2
            if matrix[row_to_search][mid_col] == target:
                return True
            elif matrix[row_to_search][mid_col] < target:
                left = mid_col + 1
            else:
                right = mid_col - 1
        return False
