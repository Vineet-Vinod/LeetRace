from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        ans = prefix = 0
        mod = 10**9 + 7
        for v in sorted(nums):
            ans = (ans + v * v * (prefix + v)) % mod
            prefix = (2 * prefix + v) % mod
        return ans
