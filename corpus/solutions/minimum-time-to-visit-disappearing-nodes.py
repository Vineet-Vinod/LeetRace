class Solution:
    def minimumTime(
        self, n: int, edges: List[List[int]], disappear: List[int]
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b, length in edges:
            graph[a].append((b, length))
            graph[b].append((a, length))
        distances = [float("inf")] * n
        distances[0] = 0
        heap = [(0, 0)]
        while heap:
            time, node = heappop(heap)
            if time != distances[node]:
                continue
            for neighbor, length in graph[node]:
                arrival = time + length
                if arrival < disappear[neighbor] and arrival < distances[neighbor]:
                    distances[neighbor] = arrival
                    heappush(heap, (arrival, neighbor))
        return [-1 if value == float("inf") else value for value in distances]
