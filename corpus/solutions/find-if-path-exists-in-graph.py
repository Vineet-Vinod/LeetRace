class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = [[] for _ in range(n)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
        seen = {source}
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return False
