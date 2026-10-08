from heapq import heappush, heappop


class Solution:
    def minCost(
        self, maxTime: int, edges: list[list[int]], passingFees: list[int]
    ) -> int:
        n = len(passingFees)
        adj = [[] for _ in range(n)]
        for a, b, t in edges:
            adj[a].append((b, t))
            adj[b].append((a, t))
        heap = [(passingFees[0], 0, 0)]
        fastest = [maxTime + 1] * n
        while heap:
            cost, time, u = heappop(heap)
            if time >= fastest[u]:
                continue
            fastest[u] = time
            if u == n - 1:
                return cost
            for v, d in adj[u]:
                if time + d <= maxTime and time + d < fastest[v]:
                    heappush(heap, (cost + passingFees[v], time + d, v))
        return -1
