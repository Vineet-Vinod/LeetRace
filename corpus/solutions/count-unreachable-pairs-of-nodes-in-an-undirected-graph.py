class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
                size[ra] += size[rb]
        roots = {}
        for node in range(n):
            root = find(node)
            roots[root] = roots.get(root, 0) + 1
        remaining = n
        answer = 0
        for component_size in roots.values():
            remaining -= component_size
            answer += component_size * remaining
        return answer
