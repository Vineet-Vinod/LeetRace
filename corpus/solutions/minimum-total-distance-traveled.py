class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robots = sorted(robot)
        n = len(robots)
        dp = [0] + [10**30] * n
        for position, limit in sorted(factory):
            nxt = dp.copy()
            for i in range(1, n + 1):
                cost = 0
                for take in range(1, min(limit, i) + 1):
                    cost += abs(robots[i - take] - position)
                    nxt[i] = min(nxt[i], dp[i - take] + cost)
            dp = nxt
        return dp[n]
