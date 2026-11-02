class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        l, r = 0, 0
        min_sub = float('inf')
        for right in range(len(s)):
            need[s[right]] -= 1
            if need[s[right]]>=0:
                missing-=1
            while missing == 0:
                if right-left+1<min_sub:
                    min_sub = right-left+1
                    l = left
                    r = right
                need[s[left]] += 1
                if need[s[left]]>0:
                    missing+=1
                left+=1
        return s[l:r+1] if  min_sub != float('inf') else ""