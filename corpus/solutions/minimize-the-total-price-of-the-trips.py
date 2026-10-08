class Solution:
    def minimumTotalPrice(
        self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]
    ) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visits = [0] * n
        for start, end in trips:
            parent = {start: -1}
            queue = [start]
            for u in queue:
                for v in adj[u]:
                    if v not in parent:
                        parent[v] = u
                        queue.append(v)
            u = end
            while u != -1:
                visits[u] += 1
                u = parent[u]

        def dfs(u, parent):
            full = price[u] * visits[u]
            half = full // 2
            for v in adj[u]:
                if v != parent:
                    a, b = dfs(v, u)
                    full += min(a, b)
                    half += a
            return full, half

        return min(dfs(0, -1))
