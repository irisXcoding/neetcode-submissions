class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sub_char_cnt = {}
        char_cnt = {}
        for item in s1:
            sub_char_cnt[item] = sub_char_cnt.get(item, 0) + 1
        for item in s2[0:len(s1)]:
            char_cnt[item] = char_cnt.get(item, 0) + 1
        if sub_char_cnt == char_cnt:
            return True
        for left in range(1, len(s2) - len(s1) + 1):
            right = left + len(s1) - 1
            if char_cnt[s2[left - 1]] > 1:
                char_cnt[s2[left - 1]] = char_cnt[s2[left - 1]] - 1
            else:
                char_cnt.pop(s2[left - 1])

            char_cnt[s2[right]] = char_cnt.get(s2[right], 0) + 1
            if sub_char_cnt == char_cnt:
                return True
        return False

