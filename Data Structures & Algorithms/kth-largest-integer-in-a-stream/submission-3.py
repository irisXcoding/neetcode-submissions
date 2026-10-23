import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.lst = []
        self.k = k
        heapq.heapify(self.lst)
        for item in nums:
            self.add(item)

    def add(self, val: int) -> int:
        if len(self.lst) < self.k:
            heapq.heappush(self.lst, val)
        elif val > self.lst[0]:
            heapq.heappop(self.lst)
            heapq.heappush(self.lst, val)
        return self.lst[0]
