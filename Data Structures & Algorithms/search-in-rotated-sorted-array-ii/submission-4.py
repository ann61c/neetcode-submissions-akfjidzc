class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                # [1,2,3,4,5,6]
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[right] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: 
                left += 1
                right -= 1
        return False

