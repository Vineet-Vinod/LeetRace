class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        offset = time % (2 * (n - 1))
        return offset + 1 if offset < n else 2 * n - 1 - offset
