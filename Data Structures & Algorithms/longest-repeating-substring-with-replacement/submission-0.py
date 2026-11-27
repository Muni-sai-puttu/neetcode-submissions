class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0

        h = {}
        for right in range(len(s)):
            h[s[right]] = h.get(s[right],0) + 1
            while (right -left +  1) - max(h.values()) > k:
                h[s[left]] -= 1
                left += 1
            max_len = max(max_len,right - left + 1)
        return max_len