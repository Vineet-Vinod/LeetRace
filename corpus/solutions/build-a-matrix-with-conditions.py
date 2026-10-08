from typing import List
from heapq import heappush, heappop


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def order(edges):
            graph = [set() for _ in range(k)]
            degree = [0] * k
            for a, b in edges:
                if b - 1 not in graph[a - 1]:
                    graph[a - 1].add(b - 1)
                    degree[b - 1] += 1
            queue = [i for i in range(k) if degree[i] == 0]
            result = []
            while queue:
                u = heappop(queue)
                result.append(u)
                for v in graph[u]:
                    degree[v] -= 1
                    if degree[v] == 0:
                        heappush(queue, v)
            return result

        rows, cols = order(rowConditions), order(colConditions)
        if len(rows) != k or len(cols) != k:
            return []
        positions = {v: i for i, v in enumerate(cols)}
        result = [[0] * k for _ in range(k)]
        for i, v in enumerate(rows):
            result[i][positions[v]] = v + 1
        return result
