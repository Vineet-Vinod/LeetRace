class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0
        units = (n + 24) // 25

        @cache
        def probability(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (
                probability(a - 4, b)
                + probability(a - 3, b - 1)
                + probability(a - 2, b - 2)
                + probability(a - 1, b - 3)
            )

        return probability(units, units)
