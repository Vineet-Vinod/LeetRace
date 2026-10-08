class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        xs = sorted(point[0] for point in points)
        rectangles = 0
        i = 0
        while i < len(xs):
            right = xs[i] + w
            rectangles += 1
            i += 1
            while i < len(xs) and xs[i] <= right:
                i += 1
        return rectangles
