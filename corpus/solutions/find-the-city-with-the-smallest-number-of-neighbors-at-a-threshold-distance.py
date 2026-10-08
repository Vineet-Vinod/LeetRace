class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        distances = [[float("inf")] * n for _ in range(n)]
        for city in range(n):
            distances[city][city] = 0
        for first, second, weight in edges:
            distances[first][second] = weight
            distances[second][first] = weight
        for middle in range(n):
            for start in range(n):
                for end in range(n):
                    distances[start][end] = min(
                        distances[start][end],
                        distances[start][middle] + distances[middle][end],
                    )
        best_city = -1
        fewest = n + 1
        for city in range(n):
            reachable = (
                sum(distance <= distanceThreshold for distance in distances[city]) - 1
            )
            if reachable <= fewest:
                fewest = reachable
                best_city = city
        return best_city
