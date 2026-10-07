class Solution:
    def maxTastiness(
        self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int
    ) -> int:
        dp = [[-1] * (maxCoupons + 1) for _ in range(maxAmount + 1)]
        dp[0][0] = 0
        for cost, taste in zip(price, tastiness):
            next_dp = [row[:] for row in dp]
            for amount in range(maxAmount + 1):
                for coupons in range(maxCoupons + 1):
                    score = dp[amount][coupons]
                    if score < 0:
                        continue
                    if amount + cost <= maxAmount:
                        next_dp[amount + cost][coupons] = max(
                            next_dp[amount + cost][coupons], score + taste
                        )
                    if coupons < maxCoupons and amount + cost // 2 <= maxAmount:
                        next_dp[amount + cost // 2][coupons + 1] = max(
                            next_dp[amount + cost // 2][coupons + 1], score + taste
                        )
            dp = next_dp
        return max(max(row) for row in dp)
