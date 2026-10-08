from collections import deque


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        distances = [[] for _ in range(n + 1)]
        distances[1] = [0]
        queue = deque([(1, 0)])
        while queue:
            u, steps = queue.popleft()
            if u == n and len(distances[n]) == 2 and steps == distances[n][1]:
                elapsed = 0
                for _ in range(steps):
                    if elapsed // change % 2:
                        elapsed = (elapsed // change + 1) * change
                    elapsed += time
                return elapsed
            for v in adj[u]:
                new = steps + 1
                if len(distances[v]) < 2 and new not in distances[v]:
                    distances[v].append(new)
                    queue.append((v, new))
        raise ValueError("Connected graph required")
