class Solution:
    def maximumScore(self, scores: list[int], edges: list[list[int]]) -> int:
        adj = [[] for _ in scores]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        adj = [sorted(xs, key=lambda x: scores[x], reverse=True)[:3] for xs in adj]
        answer = -1
        for a, b in edges:
            for c in adj[a]:
                for d in adj[b]:
                    if len({a, b, c, d}) == 4:
                        answer = max(
                            answer, scores[a] + scores[b] + scores[c] + scores[d]
                        )
        return answer
