class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        if len(numbers) == 2 and sum(numbers) == target:
            return [1,2]

        while left < right:
            while(numbers[right] > target):
                right -=1
            if numbers[right] + numbers[left] > target:
                right -=1
            elif numbers[right] + numbers[left] < target:
                left +=1
            else:
                return [left+1, right+1]
        return []