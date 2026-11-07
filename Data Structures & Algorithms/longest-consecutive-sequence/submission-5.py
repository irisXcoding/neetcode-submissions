class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for item in nums_set:
            if item -1 in nums_set:
                continue
            else:
                # find the start and count until the end
                cur_len = 0
                start = item
                while start in nums_set:
                    start+=1
                    cur_len+=1
                max_len = max(max_len, cur_len)
        return max_len