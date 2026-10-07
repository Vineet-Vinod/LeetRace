from __future__ import annotations
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min = last_max = bad = -1
        answer = 0
        for i, value in enumerate(nums):
            if value < minK or value > maxK:
                bad = i
            if value == minK:
                last_min = i
            if value == maxK:
                last_max = i
            answer += max(0, min(last_min, last_max) - bad)
        return answer
