class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph: List[List[int]] = [[] for _ in vals]
        for a, b in edges:
            graph[a].append(vals[b])
            graph[b].append(vals[a])
        answer = max(vals)
        for node, value in enumerate(vals):
            answer = max(
                answer,
                value + sum(x for x in sorted(graph[node], reverse=True)[:k] if x > 0),
            )
        return answer
