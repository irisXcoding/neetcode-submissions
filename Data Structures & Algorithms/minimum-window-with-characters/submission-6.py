class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        res = ""
        min_len = float('inf')
        t_char_dict = {}
        s_char_dict = {}
        for char in t:
            t_char_dict[char] = t_char_dict.get(char, 0) + 1
        need, have = len(t_char_dict), 0
        left = 0
        for right in range(len(s)):
            if s[right] in t_char_dict:
                s_char_dict[s[right]] = s_char_dict.get(s[right], 0) + 1
                if s_char_dict[s[right]] == t_char_dict[s[right]]:
                    have += 1
            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]
                if s[left] in t_char_dict:
                    if s_char_dict[s[left]] == t_char_dict[s[left]]:
                        have -= 1
                    s_char_dict[s[left]] -= 1
                left += 1
        return res