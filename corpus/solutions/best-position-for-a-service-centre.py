class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        import math

        if len(positions) == 1:
            return 0.0

        def vertical(x):
            lo, hi = 0.0, 100.0
            for _ in range(55):
                a = (2 * lo + hi) / 3
                b = (lo + 2 * hi) / 3
                fa = sum(math.hypot(x - px, a - py) for px, py in positions)
                fb = sum(math.hypot(x - px, b - py) for px, py in positions)
                if fa < fb:
                    hi = b
                else:
                    lo = a
            return sum(math.hypot(x - px, (lo + hi) / 2 - py) for px, py in positions)

        lo, hi = 0.0, 100.0
        for _ in range(55):
            a = (2 * lo + hi) / 3
            b = (lo + 2 * hi) / 3
            if vertical(a) < vertical(b):
                hi = b
            else:
                lo = a
        return vertical((lo + hi) / 2)
