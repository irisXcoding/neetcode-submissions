import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_neg = [-item for item in stones]
        heapq.heapify(stones_neg)
        while len(stones_neg)>1:
            item1 = heapq.heappop(stones_neg)
            item2 = heapq.heappop(stones_neg)
            if -item1>-item2:
                heapq.heappush(stones_neg, item1-item2)
            if -item2>-item2:
                heapq.heappush(stones_neg, item2-item1)
        return -stones_neg[0] if stones_neg else 0
