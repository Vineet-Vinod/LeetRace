class Solution:
    def countSubgraphsForEachDiameter(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        adjacent = [[] for _ in range(n)]
        for a, b in edges:
            adjacent[a - 1].append(b - 1)
            adjacent[b - 1].append(a - 1)
        distances = [[0] * n for _ in range(n)]
        for start in range(n):
            stack = [(start, -1, 0)]
            while stack:
                node, parent, distance = stack.pop()
                distances[start][node] = distance
                for neighbor in adjacent[node]:
                    if neighbor != parent:
                        stack.append((neighbor, node, distance + 1))
        answer = [0] * (n - 1)
        for mask in range(1, 1 << n):
            count = mask.bit_count()
            if count < 2:
                continue
            included_edges = sum(
                bool(mask & (1 << (a - 1))) and bool(mask & (1 << (b - 1)))
                for a, b in edges
            )
            if included_edges != count - 1:
                continue
            nodes = [i for i in range(n) if mask & (1 << i)]
            diameter = max(distances[a][b] for a in nodes for b in nodes)
            answer[diameter - 1] += 1
        return answer
