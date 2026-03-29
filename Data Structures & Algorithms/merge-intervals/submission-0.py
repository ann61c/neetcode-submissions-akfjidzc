class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        merged_interval = intervals[0]
        for i in range(1, len(intervals)):

            if merged_interval[1] >= intervals[i][0]:
                merged_interval = [merged_interval[0], max(merged_interval[1], intervals[i][1])]
            else:
                res.append(merged_interval)
                merged_interval = intervals[i]
        res.append(merged_interval)
        return res