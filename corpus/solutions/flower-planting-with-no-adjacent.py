class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph: List[List[int]] = [[] for _ in range(n)]
        for a, b in paths:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        answer = [0] * n
        for garden in range(n):
            used = {answer[neighbor] for neighbor in graph[garden]}
            answer[garden] = next(color for color in range(1, 5) if color not in used)
        return answer
