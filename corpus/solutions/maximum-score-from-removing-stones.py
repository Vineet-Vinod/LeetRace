class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        values = sorted((a, b, c))
        return min(sum(values) // 2, values[0] + values[1])
