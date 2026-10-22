class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        letter_count_map = {}
        start = 0
        for idx, letter in enumerate(s):
            letter_start = letter_count_map.get(letter,-1)
            if letter_start != -1:
                start = max(start, letter_start+1)
            letter_count_map[letter] = idx
            _max = max(_max, idx-start+1)
        return _max
