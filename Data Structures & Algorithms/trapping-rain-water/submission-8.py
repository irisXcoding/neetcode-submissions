class Solution:
    def trap(self, height: List[int]) -> int:
        # for height[i]: find out min(max_left, max_right)-height[i]
        # left, right
        # move the pointer with smaller height and calculate the height of it
        # loop condition: while left< right:
        # complexity: time O(n) space O(1)
        res = 0
        n = len(height)
        left, right = 0, n-1
        left_max, right_max = height[0], height[n-1]
        while left< right:
            if height[left]<height[right]:
                left+=1
                left_max = max(left_max, height[left])
                res+=max(0, min(left_max, right_max)-height[left])
            else:
                right-=1
                right_max = max(right_max, height[right])
                res+=max(0, min(left_max, right_max)-height[right])
        return res

