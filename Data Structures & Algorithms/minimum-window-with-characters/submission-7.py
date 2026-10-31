class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = Counter(t)
        missing = len(t)
        res = ""
        min_count = float('inf')
        for right, c in enumerate(s):
            need[c] = need[c]-1
            if need[c] >= 0 and c in t:
                missing -= 1
            while missing==0:
                if right-left+1<min_count:
                    min_count = right-left+1
                    res = s[left:right+1]
                need[s[left]] = need[s[left]] + 1
                if need[s[left]] > 0 and s[left] in t:
                    missing+=1
                left += 1
        return res