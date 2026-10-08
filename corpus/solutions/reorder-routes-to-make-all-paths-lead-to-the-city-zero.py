class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for source, destination in connections:
            graph[source].append((destination, 1))
            graph[destination].append((source, 0))
        changes = 0
        stack = [(0, -1)]
        while stack:
            city, parent = stack.pop()
            for neighbor, points_away in graph[city]:
                if neighbor != parent:
                    changes += points_away
                    stack.append((neighbor, city))
        return changes
