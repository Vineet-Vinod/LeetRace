from typing import List


class Solution:
    def minCost(
        self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int
    ) -> int:
        inf = 10**18
        dp = [[inf] * (n + 1) for _ in range(target + 1)]
        dp[0][0] = 0
        for i, painted in enumerate(houses):
            following = [[inf] * (n + 1) for _ in range(target + 1)]
            for groups in range(1, min(target, i + 1) + 1):
                ranked = sorted(
                    (value, color) for color, value in enumerate(dp[groups - 1])
                )[:2]
                for color in range(1, n + 1):
                    if painted and painted != color:
                        continue
                    other = ranked[0][0] if ranked[0][1] != color else ranked[1][0]
                    following[groups][color] = min(dp[groups][color], other) + (
                        cost[i][color - 1] if painted == 0 else 0
                    )
            dp = following
        answer = min(dp[target][1:])
        return answer if answer < inf else -1
