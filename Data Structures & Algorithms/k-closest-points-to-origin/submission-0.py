import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        heapq.heapify(hq)
        for point in points:
            distance = point[0]*point[0]+point[1]*point[1]
            if len(hq)<k:
                heapq.heappush(hq, (-distance, point[0], point[1]))
            else:
                if distance < -hq[0][0]:
                    heapq.heappop(hq)
                    heapq.heappush(hq, (-distance, point[0], point[1]))
        res = []
        for i in range(k):
            item = heapq.heappop(hq)
            res.append([item[1],item[2]])
        return res
