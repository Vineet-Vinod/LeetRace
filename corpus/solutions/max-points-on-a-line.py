from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 1
        for i, (x, y) in enumerate(points):
            slopes = {}
            for a, b in points[i + 1 :]:
                dx, dy = a - x, b - y
                factor = gcd(dx, dy)
                dx, dy = dx // factor, dy // factor
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[dx, dy] = slopes.get((dx, dy), 0) + 1
            answer = max(answer, 1 + max(slopes.values(), default=0))
        return answer
