class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse: List[List[int]] = [[] for _ in range(n)]
        remaining = [len(neighbors) for neighbors in graph]
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse[neighbor].append(node)
        queue = deque(i for i, degree in enumerate(remaining) if degree == 0)
        safe = []
        while queue:
            node = queue.popleft()
            safe.append(node)
            for parent in reverse[node]:
                remaining[parent] -= 1
                if remaining[parent] == 0:
                    queue.append(parent)
        return sorted(safe)
