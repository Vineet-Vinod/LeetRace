from math import isqrt
from functools import lru_cache
from collections import Counter


class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        counts = Counter(nums)
        values = tuple(sorted(counts))
        initial = tuple(counts[x] for x in values)
        adjacent = [[isqrt(a + b) ** 2 == a + b for b in values] for a in values]

        @lru_cache(None)
        def search(last: int, remaining: tuple[int, ...]) -> int:
            if not any(remaining):
                return 1
            result = 0
            for i, count in enumerate(remaining):
                if count and (last == -1 or adjacent[last][i]):
                    updated = list(remaining)
                    updated[i] -= 1
                    result += search(i, tuple(updated))
            return result

        return search(-1, initial)
