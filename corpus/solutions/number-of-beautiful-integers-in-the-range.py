from functools import lru_cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def upto(bound: int) -> int:
            if bound < 1:
                return 0
            digits = str(bound)

            @lru_cache(None)
            def dp(
                pos: int, balance: int, remainder: int, started: bool, tight: bool
            ) -> int:
                if pos == len(digits):
                    return int(started and balance == 0 and remainder == 0)
                if abs(balance) > len(digits) - pos:
                    return 0
                cap = int(digits[pos]) if tight else 9
                answer = 0
                for digit in range(cap + 1):
                    active = started or digit != 0
                    delta = (1 if digit % 2 == 0 else -1) if active else 0
                    answer += dp(
                        pos + 1,
                        balance + delta,
                        (remainder * 10 + digit) % k,
                        active,
                        tight and digit == cap,
                    )
                return answer

            return dp(0, 0, 0, False, True)

        return upto(high) - upto(low - 1)
