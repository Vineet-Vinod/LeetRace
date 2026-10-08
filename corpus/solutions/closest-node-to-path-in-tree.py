class Solution:
    def closestNode(
        self, n: int, edges: list[list[int]], query: list[list[int]]
    ) -> list[int]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        depth = [0] * n
        parent = [0] * n
        order = [0]
        for a in order:
            for b in adj[a]:
                if b != parent[a]:
                    parent[b] = a
                    depth[b] = depth[a] + 1
                    order.append(b)
        up = [parent]
        for _ in range(n.bit_length()):
            up.append([up[-1][up[-1][v]] for v in range(n)])

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            delta = depth[a] - depth[b]
            for i in range(delta.bit_length()):
                if delta >> i & 1:
                    a = up[i][a]
            if a == b:
                return a
            for row in reversed(up):
                if row[a] != row[b]:
                    a, b = row[a], row[b]
            return parent[a]

        return [
            max((lca(a, b), lca(a, c), lca(b, c)), key=lambda x: depth[x])
            for a, b, c in query
        ]
