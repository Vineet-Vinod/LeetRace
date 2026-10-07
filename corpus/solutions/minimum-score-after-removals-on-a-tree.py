class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in nums]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1] * n
        order = [0]
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        subxor = nums[:]
        size = [1] * n
        for u in reversed(order[1:]):
            subxor[parent[u]] ^= subxor[u]
            size[parent[u]] += size[u]
        # A DFS preorder gives each subtree one contiguous interval.
        preorder = []
        stack = [0]
        while stack:
            u = stack.pop()
            preorder.append(u)
            stack.extend(v for v in adj[u] if v != parent[u])
        time = [0] * n
        for i, u in enumerate(preorder):
            time[u] = i

        def ancestor(a, b):
            return time[a] <= time[b] < time[a] + size[a]

        answer = float("inf")
        for a in range(1, n):
            for b in range(a + 1, n):
                if ancestor(a, b):
                    parts = (subxor[b], subxor[a] ^ subxor[b], subxor[0] ^ subxor[a])
                elif ancestor(b, a):
                    parts = (subxor[a], subxor[b] ^ subxor[a], subxor[0] ^ subxor[b])
                else:
                    parts = (subxor[a], subxor[b], subxor[0] ^ subxor[a] ^ subxor[b])
                answer = min(answer, max(parts) - min(parts))
        return int(answer)
