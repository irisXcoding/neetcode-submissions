import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0)+1
        top_k = []
        for num, count in count_dict.items():
            if len(top_k)<k:
                heapq.heappush(top_k, (count, num))
            elif count>top_k[0][0]:
                heapq.heappop(top_k)
                heapq.heappush(top_k, (count, num))
        top_k_item = [item[1] for item in top_k]
        return top_k_item
            
