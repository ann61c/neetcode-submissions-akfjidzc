class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        res = []
        for point in points:
            x = point[0]
            y = point[1]
            # (x,y) = x**2 + y**2
            distance.append([x**2 + y**2, [x,y]])
        heapq.heapify(distance)
        for i in range(k):
            minpair = heapq.heappop(distance)[1]
            res.append(minpair)
        return res