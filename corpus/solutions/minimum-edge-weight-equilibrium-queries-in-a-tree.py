class Solution:
    def minOperationsQueries(
        self, n: int, edges: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))
        parent = [0] * n
        depth = [0] * n
        counts = [[0] * 26 for _ in range(n)]
        order = [0]
        for a in order:
            for b, w in adj[a]:
                if b != parent[a]:
                    parent[b] = a
                    depth[b] = depth[a] + 1
                    counts[b] = counts[a][:]
                    counts[b][w - 1] += 1
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

        out = []
        for a, b in queries:
            c = lca(a, b)
            length = depth[a] + depth[b] - 2 * depth[c]
            most = max(
                counts[a][i] + counts[b][i] - 2 * counts[c][i] for i in range(26)
            )
            out.append(length - most)
        return out
