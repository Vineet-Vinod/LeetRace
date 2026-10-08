from typing import List


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        dp = [1] + [0] * k
        for x in nums:
            dp = [
                (2 * dp[s] + (dp[s - x] if s >= x else 0)) % 1000000007
                for s in range(k + 1)
            ]
        return dp[k]
