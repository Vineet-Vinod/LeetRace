class Solution:
    def minimumCost(
        self, start: List[int], target: List[int], specialRoads: List[List[int]]
    ) -> int:
        points = (
            [tuple(start)]
            + [
                point
                for road in specialRoads
                for point in ((road[0], road[1]), (road[2], road[3]))
            ]
            + [tuple(target)]
        )
        distance = [10**30] * len(points)
        distance[0] = 0
        used = [False] * len(points)
        for _ in points:
            current = -1
            for i in range(len(points)):
                if not used[i] and (current == -1 or distance[i] < distance[current]):
                    current = i
            used[current] = True
            x, y = points[current]
            if points[current] == tuple(target):
                return distance[current]
            for i, (nx, ny) in enumerate(points):
                distance[i] = min(
                    distance[i], distance[current] + abs(x - nx) + abs(y - ny)
                )
            for i, road in enumerate(specialRoads):
                source = 1 + 2 * i
                destination = source + 1
                if current == source:
                    distance[destination] = min(
                        distance[destination], distance[current] + road[4]
                    )
        return distance[-1]
