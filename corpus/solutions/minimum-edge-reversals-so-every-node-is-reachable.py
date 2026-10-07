class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))
        parent = [-1] * n
        parent[0] = 0
        order = [0]
        costs = [0] * n
        for u in order:
            for v, cost in graph[u]:
                if parent[v] == -1:
                    parent[v] = u
                    costs[v] = cost
                    order.append(v)
        answer = [sum(costs)] * n
        for v in order[1:]:
            answer[v] = answer[parent[v]] + (1 if costs[v] == 0 else -1)
        return answer
