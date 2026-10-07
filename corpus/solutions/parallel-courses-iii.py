from collections import deque


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = [[] for _ in range(n)]
        degrees = [0] * n
        for a, b in relations:
            graph[a - 1].append(b - 1)
            degrees[b - 1] += 1
        queue = deque(i for i in range(n) if degrees[i] == 0)
        finish = time.copy()
        while queue:
            a = queue.popleft()
            for b in graph[a]:
                finish[b] = max(finish[b], finish[a] + time[b])
                degrees[b] -= 1
                if degrees[b] == 0:
                    queue.append(b)
        return max(finish)
