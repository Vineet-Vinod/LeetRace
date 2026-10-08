from typing import List


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        parent = list(range(n))
        size = [1] * n

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for u, v, w in edges:
            a, b = find(u), find(v)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
        cost = [-1] * n
        for u, v, w in edges:
            cost[find(u)] &= w
        return [cost[find(u)] if find(u) == find(v) else -1 for u, v in query]
