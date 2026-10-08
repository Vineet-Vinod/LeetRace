class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        for x in rods:
            updated = dp.copy()
            for difference, shorter in dp.items():
                updated[difference + x] = max(updated.get(difference + x, 0), shorter)
                nextdiff = abs(difference - x)
                updated[nextdiff] = max(
                    updated.get(nextdiff, 0), shorter + min(difference, x)
                )
            dp = updated
        return dp[0]
