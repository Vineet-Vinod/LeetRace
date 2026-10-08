class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        rank = {}

        def find(node: int) -> int:
            parent.setdefault(node, node)
            rank.setdefault(node, 0)
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(first: int, second: int) -> None:
            root_first = find(first)
            root_second = find(second)
            if root_first == root_second:
                return
            if rank[root_first] < rank[root_second]:
                root_first, root_second = root_second, root_first
            parent[root_second] = root_first
            if rank[root_first] == rank[root_second]:
                rank[root_first] += 1

        offset = 10001
        for row, column in stones:
            union(row, column + offset)
        components = {find(row) for row, _ in stones}
        return len(stones) - len(components)
