from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        left = right = 0
        res = []
        while right < len(nums):
            if (not dq) or (nums[dq[-1]] > nums[right]):
                dq.append(right)
            else:
                while dq and nums[dq[-1]] < nums[right]:
                    dq.pop()
                dq.append(right)
            if left > dq[0]:
                dq.popleft()
            if right >= k - 1:
                res.append(nums[dq[0]])
                left += 1
            right += 1
        return res
