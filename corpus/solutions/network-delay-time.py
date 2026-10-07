class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for source, target, weight in times:
            graph[source].append((target, weight))
        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        heap = [(0, k)]
        while heap:
            distance, node = heappop(heap)
            if distance != distances[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))
        result = max(distances[1:])
        return -1 if result == float("inf") else result
