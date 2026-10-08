from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = sorted(zip(nums, cost))
        half = (sum(cost) + 1) // 2
        accumulated = 0
        median = 0
        for v, c in pairs:
            accumulated += c
            if accumulated >= half:
                median = v
                break
        return sum(abs(v - median) * c for v, c in pairs)
