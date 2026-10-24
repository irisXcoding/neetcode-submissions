import heapq as hq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        top_k = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            if len(top_k) < k:
                hq.heappush(top_k, (-dist, point[0], point[1]))
            elif dist < -top_k[0][0]:
                hq.heapreplace(top_k, (-dist, point[0], point[1]))

        res = []
        while top_k:
            item = hq.heappop(top_k)
            res.append([item[1], item[2]])
        return res
