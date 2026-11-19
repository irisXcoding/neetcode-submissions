class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrace(i, path):
            # terminal condition
            if i==len(nums):
                res.append(path[:])
                return

            # option 1: choose
            path.append(nums[i])
            backtrace(i+1, path)
            # undo
            path.pop()
            # option 2: not choose
            backtrace(i+1, path)

        backtrace(0, [])
        return res
