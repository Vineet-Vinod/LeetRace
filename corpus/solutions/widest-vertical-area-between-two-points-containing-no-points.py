class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted(point[0] for point in points)
        return max(xs[index] - xs[index - 1] for index in range(1, len(xs)))
