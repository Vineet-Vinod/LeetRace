class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}
        for (a, b), value in zip(equations, values):
            graph.setdefault(a, []).append((b, value))
            graph.setdefault(b, []).append((a, 1.0 / value))
        answer = []
        for source, target in queries:
            if source not in graph or target not in graph:
                answer.append(-1.0)
                continue
            stack = [(source, 1.0)]
            visited = {source}
            result = -1.0
            while stack:
                node, product = stack.pop()
                if node == target:
                    result = product
                    break
                for neighbor, ratio in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append((neighbor, product * ratio))
            answer.append(result)
        return answer
