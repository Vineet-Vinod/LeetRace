from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] + [-1] * k
        for pile in piles:
            prefix = [0]
            for value in pile[:k]:
                prefix.append(prefix[-1] + value)
            following = dp.copy()
            for total in range(1, k + 1):
                for taken in range(1, min(total, len(pile)) + 1):
                    if dp[total - taken] >= 0:
                        following[total] = max(
                            following[total], dp[total - taken] + prefix[taken]
                        )
            dp = following
        return dp[k]
