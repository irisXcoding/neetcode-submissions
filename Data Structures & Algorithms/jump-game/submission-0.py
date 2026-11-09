class Solution:
    def canJump(self, nums: List[int]) -> bool:
        _max_idx = 0
        for idx, num in enumerate(nums):
            if idx>_max_idx:
                return False
            _max_idx = max(_max_idx, idx+num)
        return True