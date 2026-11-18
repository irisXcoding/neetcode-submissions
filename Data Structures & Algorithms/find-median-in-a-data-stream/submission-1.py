class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.min_heap and self.min_heap[0] < num:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        while  len(self.max_heap) - len(self.min_heap) > 1:
            move_num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -move_num)
        while len(self.min_heap) - len(self.max_heap) > 1:
            move_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -move_num)

    def findMedian(self) -> float:
        m = len(self.max_heap)
        n = len(self.min_heap)
        if (m + n) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0] if n>m else -self.max_heap[0]
        