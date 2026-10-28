class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max_list = [0]*n
        right_max_list = [0]*n
        l_max, r_max = 0, 0
        left_max_list[0] = height[0]
        right_max_list[n-1] = height[n-1]
        for i in range(1, n):
            left_max_list[i] = max(left_max_list[i-1], height[i])
            right_max_list[n-i-1]= max(right_max_list[n-i], height[n-i-1])
        res = 0
        for i in range(1, n):
            res+=(min(left_max_list[i], right_max_list[i])-height[i])
        return res

