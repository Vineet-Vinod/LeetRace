from __future__ import annotations


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        missing = len(t)
        left = 0
        best_start, best_length = 0, len(s) + 1
        for right, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            while missing == 0:
                length = right - left + 1
                if length < best_length:
                    best_start, best_length = left, length
                c = s[left]
                need[c] += 1
                if need[c] > 0:
                    missing += 1
                left += 1
        return "" if best_length > len(s) else s[best_start : best_start + best_length]
