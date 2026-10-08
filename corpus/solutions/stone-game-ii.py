class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def best(index: int, m: int) -> int:
            if index + 2 * m >= n:
                return suffix[index]
            return max(
                suffix[index] - best(index + x, max(m, x)) for x in range(1, 2 * m + 1)
            )

        return best(0, 1)
