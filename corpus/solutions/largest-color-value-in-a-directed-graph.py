from typing import List
from collections import deque


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            g[a].append(b)
            degree[b] += 1
        dp = [[0] * 26 for _ in range(n)]
        q = deque(i for i in range(n) if not degree[i])
        seen = 0
        ans = 0
        while q:
            v = q.popleft()
            seen += 1
            dp[v][ord(colors[v]) - 97] += 1
            ans = max(ans, max(dp[v]))
            for u in g[v]:
                for c in range(26):
                    dp[u][c] = max(dp[u][c], dp[v][c])
                degree[u] -= 1
                if not degree[u]:
                    q.append(u)
        return ans if seen == n else -1
