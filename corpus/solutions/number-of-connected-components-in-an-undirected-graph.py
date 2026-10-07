class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        components = n
        for first, second in edges:
            root_first, root_second = find(first), find(second)
            if root_first != root_second:
                parent[root_first] = root_second
                components -= 1
        return components
