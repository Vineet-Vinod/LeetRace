class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = [inf] * n
        included = [False] * n
        distances[0] = 0
        total = 0
        for _ in range(n):
            node = min(
                (i for i in range(n) if not included[i]), key=lambda i: distances[i]
            )
            included[node] = True
            total += distances[node]
            x1, y1 = points[node]
            for other in range(n):
                if not included[other]:
                    x2, y2 = points[other]
                    distances[other] = min(
                        distances[other], abs(x1 - x2) + abs(y1 - y2)
                    )
        return total
