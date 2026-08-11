class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        left, right = 0, len(height)-1
        total_area = 0
        while left<right:
            if height[left]<height[right]:
                left_max = max(height[left], left_max)
                total_area+=left_max-height[left]
                left+=1
            else:
                right_max = max(height[right], right_max)
                total_area+=right_max-height[right]
                right-=1
        return total_area
        
        