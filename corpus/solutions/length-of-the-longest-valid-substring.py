from __future__ import annotations
from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        banned = set(forbidden)
        left = answer = 0
        for right in range(len(word)):
            for length in range(1, min(10, right - left + 1) + 1):
                start = right - length + 1
                if word[start : right + 1] in banned:
                    left = start + 1
                    break
            answer = max(answer, right - left + 1)
        return answer
