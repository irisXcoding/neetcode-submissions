import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k 
        heapq.heapify(self.nums)
        for idx, item in enumerate(nums):
            if idx<k:
                heapq.heappush(self.nums, item)
            elif item>self.nums[0]:
                heapq.heappush(self.nums, item)
                heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heapq.heappush(self.nums, val)
        elif val>self.nums[0]:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
        return self.nums[0]
    
