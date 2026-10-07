from functools import lru_cache


class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        if k >= n:
            return -1
        graph = [[] for _ in range(n)]
        for a, b, toll in highways:
            graph[a].append((b, toll))
            graph[b].append((a, toll))

        @lru_cache(None)
        def visit(node, mask):
            if mask.bit_count() == k + 1:
                return 0
            answer = -1
            for other, toll in graph[node]:
                if not mask & (1 << other):
                    remaining = visit(other, mask | (1 << other))
                    if remaining >= 0:
                        answer = max(answer, toll + remaining)
            return answer

        return max(visit(i, 1 << i) for i in range(n))
