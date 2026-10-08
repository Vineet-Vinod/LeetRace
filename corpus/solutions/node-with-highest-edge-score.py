class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0] * len(edges)
        for node, target in enumerate(edges):
            scores[target] += node
        return max(range(len(edges)), key=lambda node: (scores[node], -node))
