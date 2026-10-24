class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        res = []
        for interval in sorted_intervals:
            if not res:
                res.append(interval)
            else:
                last_interval = res[-1]
                if last_interval[1]>=interval[0]:
                    mereged_interval = [last_interval[0], max(last_interval[1], interval[1])]
                    res.pop(-1)
                    res.append(mereged_interval)
                else:
                    res.append(interval)
        return res