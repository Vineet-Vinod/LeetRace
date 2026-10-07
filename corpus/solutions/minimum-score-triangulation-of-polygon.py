class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        size = len(values)
        best = [[0] * size for _ in range(size)]
        for width in range(2, size):
            for left in range(size - width):
                right = left + width
                best[left][right] = min(
                    best[left][middle]
                    + best[middle][right]
                    + values[left] * values[middle] * values[right]
                    for middle in range(left + 1, right)
                )
        return best[0][-1]
