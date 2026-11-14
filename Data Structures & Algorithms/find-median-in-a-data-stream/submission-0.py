class MedianFinder:

    def __init__(self):
        self.min_heap = []  # right part
        self.max_heap = []  # left part
        self.count = 0

    def addNum(self, num: int) -> None:

        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        self.count += 1
        # balance
        if len(self.min_heap)-len(self.max_heap)>1:
            move_item = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -move_item)
        if len(self.max_heap) - len(self.min_heap) > 1:
            move_item = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -move_item)

    def findMedian(self) -> float:
        if self.count%2==0:
            return (self.min_heap[0]-self.max_heap[0])/2
        else:
            return self.min_heap[0] if len(self.min_heap)>len(self.max_heap) else -self.max_heap[0]

