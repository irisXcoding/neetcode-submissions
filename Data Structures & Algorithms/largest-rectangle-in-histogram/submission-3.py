class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        for idx, h in enumerate(heights):
            if not stack or heights[stack[-1]]<=h:
                stack.append(idx)
            else:
                while stack and heights[stack[-1]]>h:
                    item = stack.pop()
                    if not stack:
                        left = -1
                    else:
                        left = stack[-1]
                    area = heights[item]*(idx-left-1)
                    max_area = max(area, max_area)
                stack.append(idx)

        right = len(heights)-1
        while stack:
            item = stack.pop()
            if not stack:
                left = -1
            else:
                left = stack[-1]
            area = heights[item]*(right-left)
            max_area = max(area, max_area)
        return max_area