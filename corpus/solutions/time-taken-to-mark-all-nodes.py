class Solution:
    def timeTaken(self, edges: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        parent = [-1] * n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        down = [0] * n
        top = [(0, -1, 0) for _ in range(n)]
        for u in reversed(order):
            first = second = 0
            child = -1
            for v in graph[u]:
                if parent[v] == u:
                    value = down[v] + 2 - v % 2
                    if value > first:
                        second = first
                        first = value
                        child = v
                    else:
                        second = max(second, value)
            down[u] = first
            top[u] = (first, child, second)
        up = [0] * n
        for u in order:
            first, child, second = top[u]
            for v in graph[u]:
                if parent[v] == u:
                    up[v] = max(up[u], second if v == child else first) + 2 - u % 2
        return [max(a, b) for a, b in zip(down, up)]
