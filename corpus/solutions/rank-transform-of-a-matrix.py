class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        m, n = len(matrix), len(matrix[0])
        groups = defaultdict(list)
        for i in range(m):
            for j in range(n):
                groups[matrix[i][j]].append((i, j))
        ranks = [0] * (m + n)
        answer = [[0] * n for _ in range(m)]
        for value in sorted(groups):
            parent = {}

            def find(x):
                parent.setdefault(x, x)
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            for i, j in groups[value]:
                parent[find(i)] = find(m + j)
            component_rank = {}
            for i, j in groups[value]:
                root = find(i)
                component_rank[root] = max(
                    component_rank.get(root, 0), ranks[i] + 1, ranks[m + j] + 1
                )
            for i, j in groups[value]:
                answer[i][j] = component_rank[find(i)]
            for i, j in groups[value]:
                ranks[i] = ranks[m + j] = answer[i][j]
        return answer
