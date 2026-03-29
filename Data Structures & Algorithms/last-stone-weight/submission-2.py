class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = []
        for stone in stones:
            neg_stones.append(-stone)
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            stone1 = heapq.heappop(neg_stones)
            stone2 = heapq.heappop(neg_stones)
            res = abs(stone2 - stone1)
            if res != 0:
                heapq.heappush(neg_stones,-res)
        if not neg_stones:
            return 0
        return abs(neg_stones[0])