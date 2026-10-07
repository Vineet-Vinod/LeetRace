from typing import List
from collections import deque


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        adj = [set() for _ in coins]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        queue = deque(i for i in range(n) if len(adj[i]) == 1 and not coins[i])
        remaining = n - 1
        while queue:
            u = queue.popleft()
            if not adj[u]:
                continue
            v = adj[u].pop()
            adj[v].remove(u)
            remaining -= 1
            if len(adj[v]) == 1 and not coins[v]:
                queue.append(v)
        queue = deque(i for i in range(n) if len(adj[i]) == 1)
        for _ in range(2):
            for _ in range(len(queue)):
                u = queue.popleft()
                if adj[u]:
                    v = adj[u].pop()
                    adj[v].remove(u)
                    remaining -= 1
                    if len(adj[v]) == 1:
                        queue.append(v)
        return max(0, remaining * 2)
