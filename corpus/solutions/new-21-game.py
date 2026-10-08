class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window = 1.0
        answer = 0.0
        for score in range(1, n + 1):
            dp[score] = window / maxPts
            if score < k:
                window += dp[score]
            else:
                answer += dp[score]
            expired = score - maxPts
            if expired >= 0 and expired < k:
                window -= dp[expired]
        return answer
