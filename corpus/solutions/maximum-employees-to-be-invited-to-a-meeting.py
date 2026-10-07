from collections import deque


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        depth = [1] * n
        for v in favorite:
            indegree[v] += 1
        queue = deque(i for i in range(n) if indegree[i] == 0)
        while queue:
            u = queue.popleft()
            v = favorite[u]
            depth[v] = max(depth[v], depth[u] + 1)
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
        pairs = longest = 0
        for i in range(n):
            if indegree[i] == 0:
                continue
            cycle = []
            u = i
            while indegree[u]:
                indegree[u] = 0
                cycle.append(u)
                u = favorite[u]
            if len(cycle) == 2:
                pairs += sum(depth[x] for x in cycle)
            else:
                longest = max(longest, len(cycle))
        return max(pairs, longest)
