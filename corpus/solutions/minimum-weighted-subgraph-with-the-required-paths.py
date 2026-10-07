from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumWeight(
        self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int
    ) -> int:
        forward = [[] for _ in range(n)]
        backward = [[] for _ in range(n)]
        for u, v, w in edges:
            forward[u].append((v, w))
            backward[v].append((u, w))

        def distances(source, adjacency):
            dist = [float("inf")] * n
            dist[source] = 0
            heap = [(0, source)]
            while heap:
                d, u = heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in adjacency[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        heappush(heap, (d + w, v))
            return dist

        a, b, c = (
            distances(src1, forward),
            distances(src2, forward),
            distances(dest, backward),
        )
        answer = min(x + y + z for x, y, z in zip(a, b, c))
        return -1 if answer == float("inf") else int(answer)
