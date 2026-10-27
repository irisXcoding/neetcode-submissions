class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals
        # compare: if x2<y1, merge and append, else append new interval into the res
        sorted_intervals = sorted(intervals)
        res = []
        for interval in sorted_intervals:
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                item = res.pop(-1)
                new_item = [item[0], max(item[1], interval[1])]
                res.append(new_item)
        return res