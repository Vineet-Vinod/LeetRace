from collections import defaultdict


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for u, v in pairs:
            graph[u].append(v)
            degree[u] += 1
            degree[v] -= 1
        start = min(u for u in graph)
        for u, value in degree.items():
            if value == 1:
                start = u
                break
        for edges in graph.values():
            edges.sort(reverse=True)
        stack = [start]
        route = []
        while stack:
            if graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                route.append(stack.pop())
        route.reverse()
        return [[route[i], route[i + 1]] for i in range(len(route) - 1)]
