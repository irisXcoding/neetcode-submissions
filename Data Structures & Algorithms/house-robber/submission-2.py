class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        # max_1: adjacent max_2: you can rob
        max_2, max_1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max_1
            max_1 = max(nums[i]+max_2, max_1)
            max_2 = temp
        return max(max_1, max_2)