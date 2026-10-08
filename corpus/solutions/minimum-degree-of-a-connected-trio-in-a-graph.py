class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a - 1].add(b - 1)
            adj[b - 1].add(a - 1)
        degree = list(map(len, adj))
        answer = float("inf")
        for a in range(n):
            for b in adj[a]:
                if b <= a:
                    continue
                for c in adj[a] & adj[b]:
                    if c > b:
                        answer = min(answer, degree[a] + degree[b] + degree[c] - 6)
                        if answer == 0:
                            return 0
        return -1 if answer == float("inf") else int(answer)
