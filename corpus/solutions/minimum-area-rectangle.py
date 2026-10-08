class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = {tuple(point) for point in points}
        best = None
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i + 1 :]:
                if (
                    x1 != x2
                    and y1 != y2
                    and (x1, y2) in point_set
                    and (x2, y1) in point_set
                ):
                    area = abs(x1 - x2) * abs(y1 - y2)
                    best = area if best is None else min(best, area)
        return best or 0
