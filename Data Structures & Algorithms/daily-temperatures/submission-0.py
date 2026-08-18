class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idx_gap_list = [0 for item in temperatures]
        _stack = []
        for idx, temp in enumerate(temperatures):
            if _stack:
                while _stack and _stack[-1][0]<temp:
                    old_temp, old_idx = _stack.pop(-1)
                    idx_gap_list[old_idx] = idx-old_idx
            _stack.append((temp, idx))
        return idx_gap_list
