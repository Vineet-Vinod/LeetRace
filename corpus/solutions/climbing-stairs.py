class Solution:
    def climbStairs(self, n: int) -> int:
        previous, current = 1, 1
        for _ in range(n):
            previous, current = current, previous + current
        return previous
