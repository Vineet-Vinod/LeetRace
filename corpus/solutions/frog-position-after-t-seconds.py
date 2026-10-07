from typing import List


class Solution:
    def frogPosition(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = [(1, 0, 0, 1.0)]
        for u, parent, time, probability in queue:
            children = [v for v in graph[u] if v != parent]
            if u == target:
                return probability if time == t or (time < t and not children) else 0.0
            if time < t and children:
                for v in children:
                    queue.append((v, u, time + 1, probability / len(children)))
        return 0.0
