class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_res = cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(cur+nums[i], nums[i])
            max_res = max(max_res, cur)
        return max_res