from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        adjacent = sorted(a + b for a, b in zip(weights, weights[1:]))
        if k == 1:
            return 0
        return sum(adjacent[-(k - 1) :]) - sum(adjacent[: k - 1])
