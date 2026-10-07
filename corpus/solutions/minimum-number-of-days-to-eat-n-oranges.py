from functools import cache


class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def days(x):
            if x <= 1:
                return x
            return 1 + min(x % 2 + days(x // 2), x % 3 + days(x // 3))

        return days(n)
