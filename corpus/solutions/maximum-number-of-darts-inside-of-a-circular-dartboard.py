from typing import List


class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        from math import sqrt

        radius_squared = r * r
        answer = 1

        def count(cx: float, cy: float) -> int:
            return sum(
                (x - cx) ** 2 + (y - cy) ** 2 <= radius_squared + 1e-7 for x, y in darts
            )

        for i, (x1, y1) in enumerate(darts):
            answer = max(answer, count(x1, y1))
            for x2, y2 in darts[i + 1 :]:
                dx, dy = x2 - x1, y2 - y1
                distance_squared = dx * dx + dy * dy
                if distance_squared > 4 * radius_squared:
                    continue
                scale = sqrt(max(0.0, radius_squared / distance_squared - 0.25))
                midx, midy = (x1 + x2) / 2, (y1 + y2) / 2
                answer = max(
                    answer,
                    count(midx - dy * scale, midy + dx * scale),
                    count(midx + dy * scale, midy - dx * scale),
                )
        return answer
