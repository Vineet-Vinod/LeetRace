class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        period = 2 * (n - 1)
        position = k % period
        return position if position < n else period - position
