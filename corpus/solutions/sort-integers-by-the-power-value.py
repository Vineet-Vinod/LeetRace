class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = {1: 0}

        def power(value):
            steps = 0
            current = value
            while current not in powers:
                if current % 2 == 0:
                    current //= 2
                else:
                    current = 3 * current + 1
                steps += 1
            result = steps + powers[current]
            powers[value] = result
            return result

        return sorted(range(lo, hi + 1), key=lambda value: (power(value), value))[k - 1]
