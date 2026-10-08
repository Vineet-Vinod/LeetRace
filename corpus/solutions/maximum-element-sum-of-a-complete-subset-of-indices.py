from math import isqrt


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        best = 0
        for base in range(1, len(nums) + 1):
            total = sum(
                nums[base * t * t - 1] for t in range(1, isqrt(len(nums) // base) + 1)
            )
            best = max(best, total)
        return best
