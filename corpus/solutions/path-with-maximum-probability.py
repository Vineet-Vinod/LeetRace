class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = [[] for _ in range(n)]
        for (first, second), probability in zip(edges, succProb):
            graph[first].append((second, probability))
            graph[second].append((first, probability))
        best = [0.0] * n
        best[start_node] = 1.0
        queue = [(-1.0, start_node)]
        while queue:
            negative_probability, node = heappop(queue)
            probability = -negative_probability
            if probability < best[node]:
                continue
            if node == end_node:
                return probability
            for neighbor, edge_probability in graph[node]:
                candidate = probability * edge_probability
                if candidate > best[neighbor]:
                    best[neighbor] = candidate
                    heappush(queue, (-candidate, neighbor))
        return 0.0
