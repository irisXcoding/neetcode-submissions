class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        _stack = []
        max_area = 0
        for i, h in enumerate(heights):
            while _stack and heights[_stack[-1]]>h:
                j = _stack.pop(-1)
                if not _stack:
                    left = -1
                else:
                    left = _stack[-1]
                area = heights[j]*(i-left-1)
                # print(h, area)
                max_area = max(area, max_area)
            _stack.append(i)
        # print(_stack)
        while _stack:
            j = _stack.pop(-1)
            if not _stack:
                left = -1
            else:
                left = _stack[-1]
            area = heights[j]*(i-left)
            max_area = max(area, max_area)
        return max_area
