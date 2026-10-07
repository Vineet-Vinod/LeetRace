class Solution:
    def maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int]
    ) -> int:
        graph = [[] for _ in values]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        total = sum(values)
        minimum_path = [0] * len(values)
        parent = [-1] * len(values)
        order = [0]
        for node in order:
            for child in graph[node]:
                if child != parent[node]:
                    parent[child] = node
                    order.append(child)
        for node in reversed(order):
            children = [child for child in graph[node] if parent[child] == node]
            if not children:
                minimum_path[node] = values[node]
            else:
                minimum_path[node] = min(
                    values[node], sum(minimum_path[child] for child in children)
                )
        return total - minimum_path[0]
