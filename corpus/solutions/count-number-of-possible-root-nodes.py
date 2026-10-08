from typing import List


class Solution:
    def rootCount(
        self, edges: List[List[int]], guesses: List[List[int]], k: int
    ) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        guessed = set(map(tuple, guesses))
        parent = [-1] * n
        order = [0]
        parent[0] = 0
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        counts = [0] * n
        counts[0] = sum((parent[v], v) in guessed for v in order[1:])
        for v in order[1:]:
            u = parent[v]
            counts[v] = counts[u] - ((u, v) in guessed) + ((v, u) in guessed)
        return sum(c >= k for c in counts)
