class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        n = len(colors)
        graph: list[list[int]] = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)
        sizes = [1] * n
        uniform = [True] * n
        answer = 1
        for node in reversed(order):
            for child in graph[node]:
                if parent[child] == node:
                    sizes[node] += sizes[child]
                    if not uniform[child] or colors[child] != colors[node]:
                        uniform[node] = False
            if uniform[node]:
                answer = max(answer, sizes[node])
        return answer
