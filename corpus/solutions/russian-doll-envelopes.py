from __future__ import annotations
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        from bisect import bisect_left

        tails = []
        for w, h in sorted(envelopes, key=lambda e: (e[0], -e[1])):
            i = bisect_left(tails, h)
            if i == len(tails):
                tails.append(h)
            else:
                tails[i] = h
        return len(tails)
