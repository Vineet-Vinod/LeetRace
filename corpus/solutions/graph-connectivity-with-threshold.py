from typing import List


class Solution:
    def areConnected(
        self, n: int, threshold: int, queries: List[List[int]]
    ) -> List[bool]:
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for divisor in range(threshold + 1, n + 1):
            for x in range(2 * divisor, n + 1, divisor):
                parent[find(x)] = find(divisor)
        return [find(a) == find(b) for a, b in queries]
