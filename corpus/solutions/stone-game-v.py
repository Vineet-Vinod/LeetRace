from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0]
        for v in stoneValue:
            prefix.append(prefix[-1] + v)
        dp = [[0] * n for _ in range(n)]
        left_best = [[0] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]
        for i, v in enumerate(stoneValue):
            left_best[i][i] = right_best[i][i] = v
        for left in range(n - 2, -1, -1):
            split = left - 1
            for r in range(left + 1, n):
                total = prefix[r + 1] - prefix[left]
                while split + 1 < r and 2 * (prefix[split + 2] - prefix[left]) <= total:
                    split += 1
                best = left_best[left][split] if split >= left else 0
                right_start = split + 1
                if split >= left and 2 * (prefix[split + 1] - prefix[left]) == total:
                    right_start = split + 1
                else:
                    right_start = split + 2
                if right_start <= r:
                    best = max(best, right_best[right_start][r])
                dp[left][r] = best
                left_best[left][r] = max(left_best[left][r - 1], total + best)
                right_best[left][r] = max(right_best[left + 1][r], total + best)
        return dp[0][n - 1]
