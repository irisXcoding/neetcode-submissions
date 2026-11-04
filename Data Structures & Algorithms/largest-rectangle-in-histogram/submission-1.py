class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack: idx
        # go through the heights, if h < heights(stack[-1]), h is the right boundary, pop stack, and the left boundary is the top of the stack
        stack = []
        max_area = 0
        for r_idx, h in enumerate(heights):
            if not stack or heights[stack[-1]]<h:
                stack.append(r_idx)
                continue
            while stack and heights[stack[-1]]>h:
                cur_idx = stack.pop()
                cur_h = heights[cur_idx]
                if not stack:
                    l_idx = -1
                else:
                    l_idx = stack[-1]
                area = cur_h*(r_idx-l_idx-1)
                max_area = max(max_area, area)
            stack.append(r_idx)
        n = len(heights)-1
        while stack:
            cur_idx = stack.pop()
            if not stack:
                l_idx = -1
            else:
                l_idx = stack[-1]
            area = (n-l_idx)*heights[cur_idx]
            max_area = max(max_area, area)
        return max_area
