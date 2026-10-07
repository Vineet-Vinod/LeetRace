from __future__ import annotations
from typing import List


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        negative = -(10**40)
        best = [negative] * (k + 1)
        active = [negative] * (k + 1)
        best[0] = 0
        for value in nums:
            for j in range(k, 0, -1):
                weight = (k - j + 1) * (1 if j % 2 else -1)
                active[j] = max(active[j], best[j - 1]) + weight * value
                best[j] = max(best[j], active[j])
        return best[k]
