from functools import lru_cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suffix = int(s)
        scale = 10 ** len(s)

        def upto(bound: int) -> int:
            if bound < suffix:
                return 0
            digits = str((bound - suffix) // scale)

            @lru_cache(None)
            def dp(pos: int, tight: bool) -> int:
                if pos == len(digits):
                    return 1
                cap = int(digits[pos]) if tight else 9
                return sum(
                    dp(pos + 1, tight and digit == cap)
                    for digit in range(min(cap, limit) + 1)
                )

            return dp(0, True)

        return upto(finish) - upto(start - 1)
