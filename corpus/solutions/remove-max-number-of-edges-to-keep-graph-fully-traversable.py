from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = [list(range(n + 1)), list(range(n + 1))]
        sizes = [[1] * (n + 1), [1] * (n + 1)]
        components = [n, n]

        def union(player, u, v):
            def find(node):
                while parent[player][node] != node:
                    parent[player][node] = parent[player][parent[player][node]]
                    node = parent[player][node]
                return node

            u, v = find(u), find(v)
            if u == v:
                return False
            if sizes[player][u] < sizes[player][v]:
                u, v = v, u
            parent[player][v] = u
            sizes[player][u] += sizes[player][v]
            components[player] -= 1
            return True

        used = 0
        for kind, u, v in edges:
            if kind == 3:
                alice = union(0, u, v)
                bob = union(1, u, v)
                used += alice or bob
        for kind, u, v in edges:
            if kind < 3:
                used += union(kind - 1, u, v)
        return len(edges) - used if components == [1, 1] else -1
