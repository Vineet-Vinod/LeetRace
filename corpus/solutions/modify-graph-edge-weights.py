from heapq import heappush, heappop


class Solution:
    def modifiedGraphEdges(
        self, n: int, edges: list[list[int]], source: int, destination: int, target: int
    ) -> list[list[int]]:
        result = [edge.copy() for edge in edges]
        unknown = [i for i, edge in enumerate(result) if edge[2] == -1]
        graph = [[] for _ in range(n)]
        for i, (a, b, _) in enumerate(result):
            graph[a].append((b, i))
            graph[b].append((a, i))

        def distance() -> int:
            dist = [10**30] * n
            dist[source] = 0
            heap = [(0, source)]
            while heap:
                d, a = heappop(heap)
                if d != dist[a]:
                    continue
                if a == destination:
                    return d
                for b, i in graph[a]:
                    nd = d + result[i][2]
                    if nd < dist[b]:
                        dist[b] = nd
                        heappush(heap, (nd, b))
            return 10**30

        for i in unknown:
            result[i][2] = 1
        if distance() > target:
            return []
        for i in unknown:
            result[i][2] = 2_000_000_000
        if distance() < target:
            return []
        # Fix each weight at its smallest feasible value, keeping later weights at their upper bounds.
        for i in unknown:
            result[i][2] = 1
            upper_distance = distance()
            if upper_distance < target:
                result[i][2] += target - upper_distance
        return result if distance() == target else []
