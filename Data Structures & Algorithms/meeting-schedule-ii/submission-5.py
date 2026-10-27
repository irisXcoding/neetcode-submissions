"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort
        # min heap: end of the meetings
        # new_start < heap top-> insert; else: update the end of meeting
        # complexity: time O(nlogk) k=num of meeting room, space O(n)
        # return: len(heap)
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        hq = []
        for interval in sorted_intervals:
            if not hq or hq[0]>interval.start:
                heapq.heappush(hq, interval.end)
            else:
                heapq.heapreplace(hq, interval.end)
        return len(hq)
        