class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        width = len(dungeon[0])
        dp = [10**30] * (width + 1)
        dp[width - 1] = 1
        for row in reversed(dungeon):
            for column in range(width - 1, -1, -1):
                dp[column] = max(1, min(dp[column], dp[column + 1]) - row[column])
        return dp[0]
