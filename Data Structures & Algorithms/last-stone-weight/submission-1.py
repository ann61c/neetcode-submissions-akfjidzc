class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = []
        for stone in stones:
            neg_stones.append(-stone)
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            last1 = heapq.heappop(neg_stones)
            last2 = heapq.heappop(neg_stones)
            if last1!= last2:
                heapq.heappush(neg_stones, -abs(last1 - last2))

        return -neg_stones[0] if len(neg_stones) == 1 else 0
        
        