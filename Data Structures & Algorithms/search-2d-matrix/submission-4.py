class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0]) - 1
        
        top = 0
        left = 0
        while top <= cols:
            mid = top + (cols - top) // 2
            if matrix[mid][0] > target:
                cols = mid - 1
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                return True
            if top == cols or cols - top == 1:
                while left < rows:
                    mid_num = left + (rows - left) // 2
                    if matrix[top][mid_num] > target:
                        rows = mid - 1
                    elif matrix[top][mid_num] < target:
                        left = mid + 1
                    else:
                        return True
        return False
