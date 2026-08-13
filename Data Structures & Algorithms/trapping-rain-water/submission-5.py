class Solution:
    def trap(self, height: List[int]) -> int:
        max_before = [0 for item in height]
        max_after = [0 for item in height]
        res = 0
        for idx, item in enumerate(height):
            if idx == 0:
                max_before[idx] = height[idx]
            else:
                max_before[idx] = max(max_before[idx-1], item)
        for idx in range(len(height)-1, -1, -1):
            if idx == len(height)-1:
                max_after[idx] = height[idx]
            else:
                max_after[idx] = max(max_after[idx+1], height[idx])
        for idx, item in enumerate(height):
            if min(max_before[idx], max_after[idx]) > item:
                res += min(max_before[idx], max_after[idx])-item
        return res
