class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        n = len(points)
        sign = 0
        for i in range(n):
            a, b, c = points[i], points[(i + 1) % n], points[(i + 2) % n]
            cross = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
            if cross:
                current = 1 if cross > 0 else -1
                if sign and sign != current:
                    return False
                sign = current
        return sign != 0
