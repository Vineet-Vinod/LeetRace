class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = set()
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected.add((min(a, b), max(a, b)))
        best = 0
        for a in range(n):
            for b in range(a + 1, n):
                best = max(best, degree[a] + degree[b] - ((a, b) in connected))
        return best
