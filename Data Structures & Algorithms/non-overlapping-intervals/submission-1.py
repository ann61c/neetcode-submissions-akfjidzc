class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                res+=1
                continue
            prev = intervals[i]
        return res
            