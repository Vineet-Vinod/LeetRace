class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(max(max(edge) for edge in edges) + 1))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return [a, b]
            parent[root_a] = root_b
        return []
