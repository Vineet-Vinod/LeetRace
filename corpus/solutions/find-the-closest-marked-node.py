class Solution:
    def minimumDistance(
        self, n: int, edges: List[List[int]], s: int, marked: List[int]
    ) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for source, target, weight in edges:
            graph[source].append((target, weight))
        distances = [float("inf")] * n
        distances[s] = 0
        heap = [(0, s)]
        while heap:
            distance, node = heappop(heap)
            if distance != distances[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))
        best = min((distances[node] for node in marked), default=float("inf"))
        return int(best) if best < float("inf") else -1
