class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        groups = n
        for a, b in connections:
            x, y = find(a), find(b)
            if x != y:
                parent[x] = y
                groups -= 1
        return groups - 1
