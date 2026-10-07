from typing import List


class Solution:
    def shortestPathWithHops(
        self, n: int, edges: List[List[int]], s: int, d: int, k: int
    ) -> int:
        from heapq import heappop, heappush
        from math import inf

        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        distance = [[inf] * (k + 1) for _ in range(n)]
        distance[s][0] = 0
        queue = [(0, s, 0)]
        while queue:
            cost, u, used = heappop(queue)
            if cost != distance[u][used]:
                continue
            if u == d:
                return cost
            for v, w in graph[u]:
                if cost + w < distance[v][used]:
                    distance[v][used] = cost + w
                    heappush(queue, (cost + w, v, used))
                if used < k and cost < distance[v][used + 1]:
                    distance[v][used + 1] = cost
                    heappush(queue, (cost, v, used + 1))
        raise ValueError("Graph must be connected")
