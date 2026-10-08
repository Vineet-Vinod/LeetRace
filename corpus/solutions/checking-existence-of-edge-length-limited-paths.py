from __future__ import annotations
from typing import List


class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges = sorted(edgeList, key=lambda e: e[2])
        answer = [False] * len(queries)
        j = 0
        for limit, u, v, i in sorted(
            (q[2], q[0], q[1], i) for i, q in enumerate(queries)
        ):
            while j < len(edges) and edges[j][2] < limit:
                a, b = find(edges[j][0]), find(edges[j][1])
                if a != b:
                    if size[a] < size[b]:
                        a, b = b, a
                    parent[b] = a
                    size[a] += size[b]
                j += 1
            answer[i] = find(u) == find(v)
        return answer
