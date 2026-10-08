from typing import List


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        prime = [True] * (n + 1)
        prime[0] = False
        if n:
            prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if prime[p]:
                for j in range(p * p, n + 1, p):
                    prime[j] = False
        g = [[] for _ in range(n + 1)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        size = [0] * (n + 1)
        for start in range(1, n + 1):
            if prime[start] or size[start]:
                continue
            nodes = [start]
            size[start] = -1
            for v in nodes:
                for u in g[v]:
                    if not prime[u] and not size[u]:
                        size[u] = -1
                        nodes.append(u)
            for v in nodes:
                size[v] = len(nodes)
        ans = 0
        for v in range(2, n + 1):
            if not prime[v]:
                continue
            seen = 0
            for u in g[v]:
                if not prime[u]:
                    ans += size[u] * (seen + 1)
                    seen += size[u]
        return ans
