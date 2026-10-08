class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        graph = [set() for _ in range(n + 1)]
        for a, b in corridors:
            graph[a].add(b)
            graph[b].add(a)
        answer = 0
        for a in range(1, n + 1):
            for b in graph[a]:
                if b > a:
                    answer += sum(c in graph[b] for c in graph[a] if c > b)
        return answer
