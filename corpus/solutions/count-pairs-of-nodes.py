from typing import List


class Solution:
    def countPairs(
        self, n: int, edges: List[List[int]], queries: List[int]
    ) -> List[int]:
        from collections import Counter

        degree = [0] * n
        shared = Counter()
        for u, v in edges:
            degree[u - 1] += 1
            degree[v - 1] += 1
            shared[tuple(sorted((u - 1, v - 1)))] += 1
        ordered = sorted(degree)
        answer = []
        for query in queries:
            left, right, count = 0, n - 1, 0
            while left < right:
                if ordered[left] + ordered[right] > query:
                    count += right - left
                    right -= 1
                else:
                    left += 1
            for (u, v), multiplicity in shared.items():
                if (
                    degree[u] + degree[v]
                    > query
                    >= degree[u] + degree[v] - multiplicity
                ):
                    count -= 1
            answer.append(count)
        return answer
