class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        res = []
        for idx, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(idx)
            if idx >= k - 1:
                res.append(nums[dq[0]])
            if dq[0] <= idx - k + 1:
                dq.popleft()
        return res
