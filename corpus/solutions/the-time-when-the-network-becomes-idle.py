class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        distance = [-1] * n
        distance[0] = 0
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        last = 0
        for node in range(1, n):
            round_trip = 2 * distance[node]
            last = max(
                last, round_trip + ((round_trip - 1) // patience[node]) * patience[node]
            )
        return last + 1
