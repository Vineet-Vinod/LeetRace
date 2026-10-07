class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        best = points[0][:]
        for row in points[1:]:
            left = [0] * len(row)
            left[0] = best[0]
            for col in range(1, len(row)):
                left[col] = max(left[col - 1] - 1, best[col])
            right = [0] * len(row)
            right[-1] = best[-1]
            for col in range(len(row) - 2, -1, -1):
                right[col] = max(right[col + 1] - 1, best[col])
            best = [row[col] + max(left[col], right[col]) for col in range(len(row))]
        return max(best)
