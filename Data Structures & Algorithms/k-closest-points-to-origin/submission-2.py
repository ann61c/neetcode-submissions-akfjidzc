class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)

        for point in points:
            x = point[0]
            y = point[1]
            distance = x ** 2 + y ** 2
            heapq.heappush(distances, [distance, [x,y]])
        res = []
        for i in range(k):
            res.append(heapq.heappop(distances)[1])
        return res
