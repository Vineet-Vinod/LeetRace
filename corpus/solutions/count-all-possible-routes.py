class Solution:
    def countRoutes(
        self, locations: list[int], start: int, finish: int, fuel: int
    ) -> int:
        n = len(locations)
        dp = [[0] * n for _ in range(fuel + 1)]
        for f in range(fuel + 1):
            for i in range(n):
                total = int(i == finish)
                for j in range(n):
                    cost = abs(locations[i] - locations[j])
                    if i != j and cost <= f:
                        total += dp[f - cost][j]
                dp[f][i] = total % 1000000007
        return dp[fuel][start]
