class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        from functools import lru_cache

        mod = 10**9 + 7

        def count(bound):
            digits = str(bound)

            @lru_cache(None)
            def dp(i, previous, tight):
                if i == len(digits):
                    return int(previous != -1)
                limit = int(digits[i]) if tight else 9
                result = 0
                for digit in range(limit + 1):
                    if previous == -1:
                        nxt = -1 if digit == 0 else digit
                    elif abs(previous - digit) == 1:
                        nxt = digit
                    else:
                        continue
                    result += dp(i + 1, nxt, tight and digit == limit)
                return result % mod

            return dp(0, -1, True)

        return (count(int(high)) - count(int(low) - 1)) % mod
