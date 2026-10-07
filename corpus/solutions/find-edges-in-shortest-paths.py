from heapq import heappush, heappop


class Solution:
    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]:
        graph = [[] for _ in range(n)]
        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))

        def distances(start: int) -> list[int]:
            dist = [10**30] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, a = heappop(heap)
                if d != dist[a]:
                    continue
                for b, w in graph[a]:
                    if d + w < dist[b]:
                        dist[b] = d + w
                        heappush(heap, (d + w, b))
            return dist

        ds, dt = distances(0), distances(n - 1)
        if ds[-1] == 10**30:
            return [False] * len(edges)
        return [
            ds[a] + w + dt[b] == ds[-1] or ds[b] + w + dt[a] == ds[-1]
            for a, b, w in edges
        ]
