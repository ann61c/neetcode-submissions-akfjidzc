class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                res+=1
                prev[1] = min(prev[1], intervals[i][1])
            else:
                prev = intervals[i]
        return res
        #[[1,100],[11,22],[1,11],[2,12]]
        #[1,11] [1,100] [2,12] [11,22]