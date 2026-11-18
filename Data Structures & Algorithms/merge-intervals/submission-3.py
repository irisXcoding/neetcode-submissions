class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort
        intervals.sort()
        res = []
        # compare and append
        for interval in intervals:
            if not res or res[-1][-1]<interval[0]:
                res.append(interval)
            else:
                old = res.pop(-1)
                merged_item = [old[0], max(old[1], interval[1])]
                res.append(merged_item)
        return res