class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        if max(nums) > target:
            return False
        
        
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        def dfs(index, curr_sum, res):
            if res == k:
                return True
            if curr_sum == target:
                return dfs(0, 0, res + 1)
            for i in range(index, len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                num = nums[i]
                if not visited[i]:
                    if curr_sum + num > target:
                        break
                    
                    visited[i] = True

                    if dfs(i+1, curr_sum + num, res):
                        return True
                    
                    visited[i] = False
            return False

        return dfs(0, 0, 0)