from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        incoming = [-1] * (n + 1)
        first = second = -1
        for i, (u, v) in enumerate(edges):
            if incoming[v] >= 0:
                first, second = incoming[v], i
            else:
                incoming[v] = i
        parents = list(range(n + 1))

        def find(x: int) -> int:
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        for i, (u, v) in enumerate(edges):
            if i == second:
                continue
            a, b = find(u), find(v)
            if a == b:
                return edges[first] if first >= 0 else edges[i]
            parents[b] = a
        return edges[second]
