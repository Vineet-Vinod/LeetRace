from collections import deque


class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left = [
            (r, c)
            for r in range(m)
            for c in range(n)
            if grid[r][c] and (r + c) % 2 == 0
        ]
        adj = {}
        for r, c in left:
            adj[(r, c)] = [
                (a, b)
                for a, b in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
                if 0 <= a < m and 0 <= b < n and grid[a][b]
            ]
        matched = {}
        answer = 0
        for root in left:
            queue = deque([root])
            prev = {root: None}
            seen = set()
            end = None
            while queue and end is None:
                u = queue.popleft()
                for v in adj[u]:
                    if v in seen:
                        continue
                    seen.add(v)
                    if v not in matched:
                        end = (u, v)
                        break
                    nxt = matched[v]
                    if nxt not in prev:
                        prev[nxt] = (u, v)
                        queue.append(nxt)
            if end is not None:
                u, v = end
                while True:
                    matched[v] = u
                    if prev[u] is None:
                        break
                    u, v = prev[u]
                answer += 1
        return answer
