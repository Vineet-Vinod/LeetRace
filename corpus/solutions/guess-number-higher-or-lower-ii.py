class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cost = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1
                cost[left][right] = min(
                    guess + max(cost[left][guess - 1], cost[guess + 1][right])
                    for guess in range(left, right + 1)
                )
        return cost[1][n]
