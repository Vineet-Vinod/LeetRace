import math


class Solution:
    def visiblePoints(
        self, points: List[List[int]], angle: int, location: List[int]
    ) -> int:
        coincident = 0
        directions = []
        for x, y in points:
            dx, dy = x - location[0], y - location[1]
            if dx == dy == 0:
                coincident += 1
            else:
                directions.append(math.atan2(dy, dx))
        directions.sort()
        n = len(directions)
        directions += [v + 2 * math.pi for v in directions]
        width = math.radians(angle)
        left = 0
        answer = 0
        for right, direction in enumerate(directions):
            while direction - directions[left] > width + 1e-12 or right - left + 1 > n:
                left += 1
            answer = max(answer, right - left + 1)
        return answer + coincident
