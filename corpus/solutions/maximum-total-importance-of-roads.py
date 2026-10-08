class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for first, second in roads:
            degree[first] += 1
            degree[second] += 1
        degree.sort()
        return sum(rank * count for rank, count in enumerate(degree, start=1))
