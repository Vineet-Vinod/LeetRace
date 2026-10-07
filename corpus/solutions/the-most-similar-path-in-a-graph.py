from typing import List


class Solution:
    def mostSimilar(
        self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]
    ) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        length = len(targetPath)
        dp = [[0] * n for _ in range(length)]
        dp[-1] = [int(name != targetPath[-1]) for name in names]
        for i in range(length - 2, -1, -1):
            for node in range(n):
                dp[i][node] = int(names[node] != targetPath[i]) + min(
                    dp[i + 1][nxt] for nxt in adj[node]
                )
        node = min(range(n), key=lambda x: (dp[0][x], x))
        answer = [node]
        for i in range(1, length):
            node = min(adj[node], key=lambda x: (dp[i][x], x))
            answer.append(node)
        return answer
