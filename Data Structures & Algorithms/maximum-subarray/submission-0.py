class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = best = nums[0]
        for num in nums[1:]:
            cur = max(cur+num, num) # start from num if num>cur+num
            best = max(best, cur)
        return best