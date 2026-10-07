from typing import List


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = [set() for _ in range(n + 1)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        odd = [i for i in range(1, n + 1) if len(adj[i]) % 2]
        if not odd:
            return True
        if len(odd) == 2:
            a, b = odd
            return b not in adj[a] or any(
                i != a and i != b and i not in adj[a] and i not in adj[b]
                for i in range(1, n + 1)
            )
        if len(odd) == 4:
            a, b, c, d = odd
            return any(
                v not in adj[u] and y not in adj[x]
                for u, v, x, y in [(a, b, c, d), (a, c, b, d), (a, d, b, c)]
            )
        return False
