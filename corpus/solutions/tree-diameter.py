class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(len(edges) + 1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def farthest(start):
            distances = [-1] * len(graph)
            distances[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if distances[neighbor] < 0:
                        distances[neighbor] = distances[node] + 1
                        queue.append(neighbor)
            endpoint = max(range(len(graph)), key=lambda node: distances[node])
            return endpoint, distances[endpoint]

        endpoint, _ = farthest(0)
        return farthest(endpoint)[1]
