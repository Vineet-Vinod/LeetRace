from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        prev = 0
        ans = 0
        for a, b in zip(nums, target):
            d = b - a
            ans += max(0, abs(d) - abs(prev)) if d * prev > 0 else abs(d)
            prev = d
        return ans
