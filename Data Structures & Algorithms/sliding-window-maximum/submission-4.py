class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        heapq.heapify(max_heap)
        res = []
        for idx, item in enumerate(nums):
            heapq.heappush(max_heap, [-item, idx])
            if idx >= k-1:
                while max_heap[0][1] < idx - k +1:
                    heapq.heappop(max_heap)
                max_item, max_idx = max_heap[0]
                res.append(-max_item)
        return res

            

                




        