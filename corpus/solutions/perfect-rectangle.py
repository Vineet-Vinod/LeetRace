class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        corners: set[tuple[int, int]] = set()
        area = 0
        x1 = y1 = 100001
        x2 = y2 = -100001
        for x, y, a, b in rectangles:
            x1, y1, x2, y2 = min(x1, x), min(y1, y), max(x2, a), max(y2, b)
            area += (a - x) * (b - y)
            for point in ((x, y), (x, b), (a, y), (a, b)):
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)
        return area == (x2 - x1) * (y2 - y1) and corners == {
            (x1, y1),
            (x1, y2),
            (x2, y1),
            (x2, y2),
        }
