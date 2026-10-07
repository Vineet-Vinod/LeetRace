from typing import List


class Solution:
    def checkContradictions(
        self, equations: List[List[str]], values: List[float]
    ) -> bool:
        parent = {}
        weight = {}

        def find(x):
            if parent[x] != x:
                p = parent[x]
                parent[x] = find(p)
                weight[x] *= weight[p]
            return parent[x]

        for (a, b), value in zip(equations, values):
            for x in (a, b):
                if x not in parent:
                    parent[x], weight[x] = x, 1.0
            ra, rb = find(a), find(b)
            if ra == rb:
                if abs(weight[a] / weight[b] - value) >= 1e-5:
                    return True
            else:
                parent[ra] = rb
                weight[ra] = value * weight[b] / weight[a]
        return False
