from __future__ import annotations
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        import heapq

        adj = [[] for _ in range(n)]
        for a, b, count in edges:
            adj[a].append((b, count + 1))
            adj[b].append((a, count + 1))
        dist = [10**30] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            d, a = heapq.heappop(heap)
            if d != dist[a]:
                continue
            for b, w in adj[a]:
                if d + w < dist[b]:
                    dist[b] = d + w
                    heapq.heappush(heap, (d + w, b))
        answer = sum(d <= maxMoves for d in dist)
        for a, b, count in edges:
            answer += min(
                count, max(0, maxMoves - dist[a]) + max(0, maxMoves - dist[b])
            )
        return answer
