from typing import List


class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        adj = [[] for _ in cost]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1] * n
        order = [0]
        for node in order:
            for child in adj[node]:
                if child != parent[node]:
                    parent[child] = node
                    order.append(child)
        values = [[v] for v in cost]
        size = [1] * n
        answer = [1] * n
        for node in reversed(order):
            vals = sorted(values[node])
            if size[node] >= 3:
                answer[node] = max(
                    0, vals[-1] * vals[-2] * vals[-3], vals[0] * vals[1] * vals[-1]
                )
            if parent[node] >= 0:
                p = parent[node]
                size[p] += size[node]
                values[p].extend(vals if len(vals) <= 5 else vals[:2] + vals[-3:])
        return answer
