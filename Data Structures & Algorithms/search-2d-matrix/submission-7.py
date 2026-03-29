class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        low = 0 
        high = width * height - 1
        while low <= high:
            mid = low + (high - low) // 2
            val = matrix[mid//width][mid%width]
            if val < target:
                low = mid + 1
            elif val > target:
                high = mid - 1
            else:
                return True
        return False

                        

