from typing import List


class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        degree = [len(neighbors) for neighbors in graph]
        queue = deque(i for i, value in enumerate(degree) if value == 1)
        while queue:
            node = queue.popleft()
            degree[node] = 0
            for neighbor in graph[node]:
                if degree[neighbor] > 0:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        answer = [-1] * n
        queue = deque(i for i, value in enumerate(degree) if value > 0)
        for node in queue:
            answer[node] = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if answer[neighbor] < 0:
                    answer[neighbor] = answer[node] + 1
                    queue.append(neighbor)
        return answer
