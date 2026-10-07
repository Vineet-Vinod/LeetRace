class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:
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
        sums = values[:]
        answer = 0
        for u in reversed(order):
            if sums[u] % k == 0:
                answer += 1
            elif parent[u] >= 0:
                sums[parent[u]] += sums[u]
        return answer
