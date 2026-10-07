class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        visited = [False] * len(edges)
        answer = -1
        for start in range(len(edges)):
            path = {}
            v = start
            while v != -1 and not visited[v]:
                visited[v] = True
                path[v] = len(path)
                v = edges[v]
            if v in path:
                answer = max(answer, len(path) - path[v])
        return answer
