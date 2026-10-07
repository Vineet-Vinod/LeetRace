class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        base = [[10**9] * n for _ in range(n)]
        for i in range(n):
            base[i][i] = 0
        for u, v, w in roads:
            base[u][v] = base[v][u] = min(base[u][v], w)
        answer = 0
        for mask in range(1 << n):
            nodes = [i for i in range(n) if mask >> i & 1]
            distance = [row[:] for row in base]
            for mid in nodes:
                for i in nodes:
                    for j in nodes:
                        distance[i][j] = min(
                            distance[i][j], distance[i][mid] + distance[mid][j]
                        )
            if all(distance[i][j] <= maxDistance for i in nodes for j in nodes):
                answer += 1
        return answer
