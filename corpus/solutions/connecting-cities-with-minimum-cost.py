class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        total = 0
        used = 0
        for a, b, cost in sorted(connections, key=lambda edge: edge[2]):
            ra, rb = find(a), find(b)
            if ra != rb:
                if size[ra] < size[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                size[ra] += size[rb]
                total += cost
                used += 1
                if used == n - 1:
                    return total
        return 0 if n == 1 else -1
