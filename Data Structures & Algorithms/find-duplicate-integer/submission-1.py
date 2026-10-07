class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find the meeting point
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # find the entrance of the cycle
        slow_1 = 0
        while True:
            slow = nums[slow]
            slow_1 = nums[slow_1]
            if slow == slow_1:
                break
        return slow