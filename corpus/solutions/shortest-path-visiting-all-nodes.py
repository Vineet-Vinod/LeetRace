from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        full = (1 << n) - 1
        q = deque((v, 1 << v, 0) for v in range(n))
        seen = {(v, 1 << v) for v in range(n)}
        while q:
            v, mask, d = q.popleft()
            if mask == full:
                return d
            for u in graph[v]:
                state = (u, mask | 1 << u)
                if state not in seen:
                    seen.add(state)
                    q.append((*state, d + 1))
        return -1
