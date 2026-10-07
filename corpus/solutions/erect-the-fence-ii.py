import math
import random


class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[float]:
        points = [(float(x), float(y)) for x, y in trees]
        random.Random(0).shuffle(points)

        def inside(c: tuple[float, float, float], p: tuple[float, float]) -> bool:
            return math.hypot(p[0] - c[0], p[1] - c[1]) <= c[2] + 1e-8

        def diameter(
            p: tuple[float, float], q: tuple[float, float]
        ) -> tuple[float, float, float]:
            x, y = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
            return x, y, math.hypot(p[0] - q[0], p[1] - q[1]) / 2

        def cross(
            p: tuple[float, float], q: tuple[float, float], r: tuple[float, float]
        ) -> float:
            return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

        def circumcircle(
            p: tuple[float, float], q: tuple[float, float], r: tuple[float, float]
        ) -> tuple[float, float, float] | None:
            ax, ay = q[0] - p[0], q[1] - p[1]
            bx, by = r[0] - p[0], r[1] - p[1]
            d = 2 * (ax * by - ay * bx)
            if d == 0:
                return None
            a2, b2 = ax * ax + ay * ay, bx * bx + by * by
            x, y = p[0] + (by * a2 - ay * b2) / d, p[1] + (ax * b2 - bx * a2) / d
            return x, y, math.hypot(x - p[0], y - p[1])

        def two_boundary(
            prefix: list[tuple[float, float]],
            p: tuple[float, float],
            q: tuple[float, float],
        ) -> tuple[float, float, float]:
            base = diameter(p, q)
            left: tuple[float, float, float] | None = None
            right: tuple[float, float, float] | None = None
            for r in prefix:
                if inside(base, r):
                    continue
                side = cross(p, q, r)
                c = circumcircle(p, q, r)
                if c is None:
                    continue
                center = (c[0], c[1])
                if side > 0 and (
                    left is None
                    or cross(p, q, center) > cross(p, q, (left[0], left[1]))
                ):
                    left = c
                elif side < 0 and (
                    right is None
                    or cross(p, q, center) < cross(p, q, (right[0], right[1]))
                ):
                    right = c
            choices = [c for c in (left, right) if c is not None]
            return min(choices, key=lambda c: c[2]) if choices else base

        circle = (points[0][0], points[0][1], 0.0)
        for i, p in enumerate(points):
            if inside(circle, p):
                continue
            circle = (p[0], p[1], 0.0)
            for j, q in enumerate(points[:i]):
                if not inside(circle, q):
                    circle = (
                        diameter(p, q)
                        if circle[2] == 0
                        else two_boundary(points[:j], p, q)
                    )
        return list(circle)
