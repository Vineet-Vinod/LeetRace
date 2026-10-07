class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        pivot = math.isqrt(total)
        return pivot if pivot * pivot == total else -1
