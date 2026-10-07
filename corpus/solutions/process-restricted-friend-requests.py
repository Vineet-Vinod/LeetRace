class Solution:
    def friendRequests(
        self, n: int, restrictions: list[list[int]], requests: list[list[int]]
    ) -> list[bool]:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        result = []
        for u, v in requests:
            a, b = find(u), find(v)
            allowed = a == b or all(
                {find(x), find(y)} != {a, b} for x, y in restrictions
            )
            result.append(allowed)
            if allowed:
                parent[a] = b
        return result
