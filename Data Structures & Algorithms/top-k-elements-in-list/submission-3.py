class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict for value:count
        # list for bucket which index is the count
        # return items from the end of the list
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0)+1
        n = max(count_dict.values())
        bucket_list = [[]for i in range(n+1)]
        for num, count in count_dict.items():
            bucket_list[count].append(num)
        res = []
        for i in range(n, -1,-1):
            res.extend(bucket_list[i])
            if len(res)>=k:
                return res[:k]

            