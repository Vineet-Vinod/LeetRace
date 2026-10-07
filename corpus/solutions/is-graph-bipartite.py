class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        for start in range(len(graph)):
            if colors[start] != 0:
                continue
            colors[start] = 1
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == colors[node]:
                        return False
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)
        return True
