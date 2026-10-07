class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points: set[tuple[int, int]] = set()
        for x, y, radius in circles:
            for px in range(x - radius, x + radius + 1):
                for py in range(y - radius, y + radius + 1):
                    if (px - x) ** 2 + (py - y) ** 2 <= radius * radius:
                        points.add((px, py))
        return len(points)
