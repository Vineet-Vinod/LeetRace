from functools import lru_cache


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10**9 + 7

        def upto(bound: int) -> int:
            if bound < 1:
                return 0
            digits = str(bound)

            @lru_cache(None)
            def dp(pos: int, total: int, tight: bool) -> int:
                if total > max_sum:
                    return 0
                if pos == len(digits):
                    return int(min_sum <= total <= max_sum)
                cap = int(digits[pos]) if tight else 9
                return (
                    sum(
                        dp(pos + 1, total + digit, tight and digit == cap)
                        for digit in range(cap + 1)
                    )
                    % mod
                )

            return dp(0, 0, True)

        return (upto(int(num2)) - upto(int(num1) - 1)) % mod
