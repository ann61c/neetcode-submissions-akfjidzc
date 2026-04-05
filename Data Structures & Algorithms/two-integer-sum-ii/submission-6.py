class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1

        while left < right:
            while numbers[right] > target:
                right-=1
            while left < right and left + right < target:
                left+=1
            while left < right and left + right > target:
                right-=1
            if left + right == target:
                return [left, right]
        return []
