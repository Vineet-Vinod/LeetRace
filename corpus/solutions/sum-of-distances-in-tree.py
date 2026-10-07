from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)
        sizes = [1] * n
        answer = [0] * n
        for node in reversed(order[1:]):
            sizes[parent[node]] += sizes[node]
            answer[parent[node]] += answer[node] + sizes[node]
        for node in order[1:]:
            answer[node] = answer[parent[node]] + n - 2 * sizes[node]
        return answer
