from collections import deque


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        color = [-1] * n
        answer = 0
        for start in range(n):
            if color[start] >= 0:
                continue
            color[start] = 0
            component = [start]
            for u in component:
                for v in adj[u]:
                    if color[v] < 0:
                        color[v] = color[u] ^ 1
                        component.append(v)
                    elif color[v] == color[u]:
                        return -1
            best = 0
            for source in component:
                distance = {source: 0}
                queue = deque([source])
                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if v not in distance:
                            distance[v] = distance[u] + 1
                            queue.append(v)
                best = max(best, max(distance.values()) + 1)
            answer += best
        return answer
