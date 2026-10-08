class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        modulo = 10**9 + 7
        graph = [[] for _ in range(n)]
        for start, end, time in roads:
            graph[start].append((end, time))
            graph[end].append((start, time))
        distances = [float("inf")] * n
        ways = [0] * n
        distances[0] = 0
        ways[0] = 1
        queue = [(0, 0)]
        while queue:
            distance, node = heappop(queue)
            if distance != distances[node]:
                continue
            for neighbor, time in graph[node]:
                candidate = distance + time
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    ways[neighbor] = ways[node]
                    heappush(queue, (candidate, neighbor))
                elif candidate == distances[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % modulo
        return ways[-1]
