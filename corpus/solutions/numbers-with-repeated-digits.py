from functools import lru_cache


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = tuple(int(c) for c in str(n))

        @lru_cache(None)
        def count(i: int, mask: int, tight: bool) -> int:
            if i == len(digits):
                return int(mask != 0)
            limit = digits[i] if tight else 9
            total = 0
            for d in range(limit + 1):
                if mask == 0 and d == 0:
                    total += count(i + 1, 0, tight and d == limit)
                elif not mask >> d & 1:
                    total += count(i + 1, mask | 1 << d, tight and d == limit)
            return total

        return n - count(0, 0, True)
