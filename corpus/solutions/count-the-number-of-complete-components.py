class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = set()
        answer = 0
        for start in range(n):
            if start in seen:
                continue
            stack = [start]
            seen.add(start)
            vertices = []
            degree_sum = 0
            while stack:
                node = stack.pop()
                vertices.append(node)
                degree_sum += len(graph[node])
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            if degree_sum == len(vertices) * (len(vertices) - 1):
                answer += 1
        return answer
