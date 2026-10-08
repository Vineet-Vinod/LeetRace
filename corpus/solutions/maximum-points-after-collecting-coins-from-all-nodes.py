from typing import List


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1] * n
        parent[0] = 0
        order = [0]
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        limit = max(coins).bit_length()
        dp = [[0] * (limit + 1) for _ in range(n)]
        for u in reversed(order):
            for shift in range(limit - 1, -1, -1):
                full = (coins[u] >> shift) - k
                half = coins[u] >> (shift + 1)
                for v in adj[u]:
                    if parent[v] == u:
                        full += dp[v][shift]
                        half += dp[v][shift + 1]
                dp[u][shift] = max(full, half)
        return dp[0][0]
