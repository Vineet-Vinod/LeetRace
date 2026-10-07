from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        positions = [0] + sorted(cuts) + [n]
        size = len(positions)
        dp = [[0] * size for _ in positions]
        for width in range(2, size):
            for left in range(size - width):
                right = left + width
                dp[left][right] = (
                    positions[right]
                    - positions[left]
                    + min(
                        dp[left][mid] + dp[mid][right] for mid in range(left + 1, right)
                    )
                )
        return dp[0][-1]
