class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub_char_cnt = {}
        char_cnt = {}
        for item in s1:
            sub_char_cnt[item] = sub_char_cnt.get(item, 0)+1
        print(sub_char_cnt)
        for left in range(0, len(s2)-len(s1)+1):
            for right in range(left, left+len(s1)):
                char_cnt[s2[right]] = char_cnt.get(s2[right], 0)+1
            print(char_cnt)
            if sub_char_cnt==char_cnt:
                return True
            char_cnt = {}
        return False
