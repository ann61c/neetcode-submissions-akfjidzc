class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)
        
        while len(neg_stones) > 1:
            stone1 = heapq.heappop(neg_stones)
            stone2 = heapq.heappop(neg_stones)
            
            if stone1 != stone2:
                heapq.heappush(neg_stones,stone1 - stone2)
        return -neg_stones[0] if neg_stones else 0