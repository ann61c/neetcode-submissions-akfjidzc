class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        previous = intervals[0]
        res = 0
        #[1,2] [1,4] [2,4]
        for i in range(1, len(intervals)):
            if previous[1] >= intervals[i][0]:
                res += 1
            else:
                previous= intervals[i]
        return res - 1
            