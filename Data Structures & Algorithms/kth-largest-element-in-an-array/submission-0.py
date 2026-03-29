class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = []
        for num in nums:
            neg_nums.append(-num)
        heapq.heapify(neg_nums)
        for i in range(k - 1):
            heapq.heappop(neg_nums)
        return -neg_nums[0]