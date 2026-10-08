from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1] * n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        # down includes both endpoints; trimmed excludes the far endpoint.
        down = price.copy()
        trimmed = [0] * n
        answer = 0
        for u in reversed(order):
            for v in graph[u]:
                if parent[v] != u:
                    continue
                answer = max(answer, down[u] + trimmed[v], trimmed[u] + down[v])
                down[u] = max(down[u], price[u] + down[v])
                trimmed[u] = max(trimmed[u], price[u] + trimmed[v])
        return answer
