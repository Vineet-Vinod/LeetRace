class Solution:
    def findDerangement(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 0
        previous_previous, previous = 1, 0
        for size in range(2, n + 1):
            current = (size - 1) * (previous + previous_previous) % mod
            previous_previous, previous = previous, current
        return previous
