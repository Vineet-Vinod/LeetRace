from __future__ import annotations
from typing import List


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        from collections import Counter

        return len(nums) >= max(Counter(nums).values()) * k
