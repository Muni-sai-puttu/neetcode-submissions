from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        need = len(target)
        have = 0
        left = 0
        window = {}
        res = [-1,-1]
        min_len = float('inf')
        for right in range(len(s)):
            ans = s[right]
            window[s[right]] = window.get(s[right],0) + 1
            if ans in target and target[ans] == window[ans]:
                have += 1
            while have == need:
                if right - left + 1 < min_len:
                    min_len = right -left + 1
                    res = [left,right]
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1
        l,r = res
        return s[l:r+1] if min_len != float('inf') else ""