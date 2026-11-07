class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _dict = {}
        left = 0
        res = 0
        for right, c in enumerate(s):
            _dict[c] = _dict.get(c, 0)+1
            # find repeat, shrink left
            while _dict.get(c)>1:
                res = max(res, right-left)
                _dict[s[left]] = _dict.get(s[left], 0) - 1
                left+=1
        res = max(res, len(s) - left)
        return res