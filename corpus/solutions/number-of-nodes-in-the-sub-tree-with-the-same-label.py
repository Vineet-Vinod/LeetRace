class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph: List[List[int]] = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)
        counts = [[0] * 26 for _ in range(n)]
        answer = [0] * n
        for node in reversed(order):
            label = ord(labels[node]) - ord("a")
            counts[node][label] += 1
            answer[node] = counts[node][label]
            if parent[node] != -1:
                parent_counts = counts[parent[node]]
                for index in range(26):
                    parent_counts[index] += counts[node][index]
        return answer
