class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            value = n
            total = 0
            factor = 2
            while factor * factor <= value:
                while value % factor == 0:
                    total += factor
                    value //= factor
                factor += 1
            if value > 1:
                total += value
            if total == n:
                return n
            n = total
