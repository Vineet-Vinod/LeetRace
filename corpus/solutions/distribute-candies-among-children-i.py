class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return sum(
            0 <= first <= limit
            and 0 <= second <= limit
            and 0 <= n - first - second <= limit
            for first in range(n + 1)
            for second in range(n + 1)
        )
