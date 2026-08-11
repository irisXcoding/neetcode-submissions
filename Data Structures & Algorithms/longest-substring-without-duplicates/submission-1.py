class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exist_dict = {}
        l, r =0,0
        max_l = 0
        while r <len(s):
            if s[r] in exist_dict and exist_dict[s[r]]>=l:
                l = exist_dict[s[r]]+1
            exist_dict[s[r]] = r
            cur_l = r-l+1
            r+=1
            max_l = max(cur_l, max_l)
        return max_l
                


