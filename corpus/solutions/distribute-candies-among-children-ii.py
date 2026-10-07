class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def choose2(value: int) -> int:
            return value * (value - 1) // 2 if value >= 2 else 0

        total = choose2(n + 2)
        for count in range(1, 4):
            remaining = n - count * (limit + 1)
            term = choose2(remaining + 2)
            total += (-1 if count % 2 else 1) * (3 if count != 2 else 3) * term
        return total
