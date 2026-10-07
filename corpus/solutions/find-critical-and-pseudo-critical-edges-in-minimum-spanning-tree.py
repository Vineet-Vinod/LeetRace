from __future__ import annotations
from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        ordered = sorted((w, a, b, i) for i, (a, b, w) in enumerate(edges))

        def mst(skip=-1, force=-1):
            parent = list(range(n))

            def find(x):
                while x != parent[x]:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            total = count = 0
            if force >= 0:
                a, b, w = edges[force]
                parent[a] = b
                total = w
                count = 1
            for w, a, b, i in ordered:
                if i == skip:
                    continue
                a, b = find(a), find(b)
                if a != b:
                    parent[a] = b
                    total += w
                    count += 1
            return total if count == n - 1 else 10**20

        base = mst()
        critical, pseudo = [], []
        for i in range(len(edges)):
            if mst(skip=i) > base:
                critical.append(i)
            elif mst(force=i) == base:
                pseudo.append(i)
        return [critical, pseudo]
