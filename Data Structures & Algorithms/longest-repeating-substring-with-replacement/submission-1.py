class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_cnt = {}
        max_freq = 0
        max_length = 0
        for right, char in enumerate(s):
            char_cnt[char] = char_cnt.get(char, 0)+1
            if char_cnt[char]> max_freq:
                max_freq = char_cnt[char]
            while right-left+1-max_freq>k and right<len(s):
                char_cnt[s[left]] = char_cnt.get(s[left], 0)-1
                max_freq = max(char_cnt.values()) if char_cnt.values() else 0
                left+=1
            max_length = max(max_length, right-left+1)
        return max_length
            
