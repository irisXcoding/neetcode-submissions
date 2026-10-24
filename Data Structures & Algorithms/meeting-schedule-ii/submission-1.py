import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x:x.start)
        rooms = []
        heapq.heapify(rooms)
        for interval in sorted_intervals:
            if not rooms or interval.start<rooms[0]:
                heapq.heappush(rooms, interval.end)
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval.end)
        return len(rooms)
            
        