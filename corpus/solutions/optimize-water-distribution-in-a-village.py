class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        edges = [(c, i + 1, 0) for i, c in enumerate(wells)]
        edges.extend((c, a, b) for a, b, c in pipes)
        parent = list(range(n + 1))

        def find(i: int) -> int:
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        result = 0
        for c, a, b in sorted(edges):
            a, b = find(a), find(b)
            if a != b:
                parent[a] = b
                result += c
        return result
