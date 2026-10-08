from typing import List
from collections import deque


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        best = n + 1
        for start in range(n):
            distance, parent = [-1] * n, [-1] * n
            distance[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                if 2 * distance[u] + 1 >= best:
                    continue
                for v in graph[u]:
                    if distance[v] == -1:
                        distance[v], parent[v] = distance[u] + 1, u
                        queue.append(v)
                    elif parent[u] != v:
                        best = min(best, distance[u] + distance[v] + 1)
            if best == 3:
                break
        return best if best <= n else -1
