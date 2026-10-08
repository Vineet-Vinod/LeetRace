class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        from collections import Counter

        def digit_sum(value: int) -> int:
            total = 0
            while value:
                total += value % 10
                value //= 10
            return total

        counts = Counter(digit_sum(value) for value in range(lowLimit, highLimit + 1))
        return max(counts.values())
