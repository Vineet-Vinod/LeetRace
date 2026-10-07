class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for a, b, distance in roads:
            graph[a - 1].append((b - 1, distance))
            graph[b - 1].append((a - 1, distance))
        seen = {0}
        stack = [0]
        answer = 10**30
        while stack:
            node = stack.pop()
            for neighbor, distance in graph[node]:
                answer = min(answer, distance)
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return answer
