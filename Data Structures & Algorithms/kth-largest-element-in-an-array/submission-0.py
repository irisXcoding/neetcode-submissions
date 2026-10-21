import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        heapq.heapify(hq)
        for item in nums:
            if len(hq)<k:
                heapq.heappush(hq, item)
            elif item>hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, item)
        return hq[0]