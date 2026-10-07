class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        groups: dict[tuple[int, int, int], list[tuple[int, int]]] = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                key = (x1 + x2, y1 + y2, (x1 - x2) ** 2 + (y1 - y2) ** 2)
                groups[key].append((i, j))
        point_set = [tuple(point) for point in points]
        best = float("inf")
        for pairs in groups.values():
            for i in range(len(pairs)):
                a, b = pairs[i]
                for j in range(i + 1, len(pairs)):
                    c, d = pairs[j]
                    p1, p2, p3 = point_set[a], point_set[b], point_set[c]
                    area = abs(
                        (p1[0] - p3[0]) * (p2[1] - p3[1])
                        - (p1[1] - p3[1]) * (p2[0] - p3[0])
                    )
                    if area:
                        best = min(best, area)
        return 0.0 if best == float("inf") else float(best)
