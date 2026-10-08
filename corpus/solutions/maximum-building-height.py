class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        limits = sorted([[1, 0], *[r[:] for r in restrictions]])
        for i in range(1, len(limits)):
            limits[i][1] = min(
                limits[i][1], limits[i - 1][1] + limits[i][0] - limits[i - 1][0]
            )
        for i in range(len(limits) - 2, -1, -1):
            limits[i][1] = min(
                limits[i][1], limits[i + 1][1] + limits[i + 1][0] - limits[i][0]
            )
        answer = limits[-1][1] + n - limits[-1][0]
        for (a, h), (b, g) in zip(limits, limits[1:]):
            answer = max(answer, (h + g + b - a) // 2)
        return answer
