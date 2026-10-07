from heapq import heappop, heappush


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        names = sorted(set(original + changed))
        indices = {name: i for i, name in enumerate(names)}
        graph: list[dict[int, int]] = [{} for _ in names]
        for a, b, c in zip(original, changed, cost):
            i, j = indices[a], indices[b]
            graph[i][j] = min(graph[i].get(j, 10**30), c)
        distances = []
        for start in range(len(names)):
            dist = [10**30] * len(names)
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, i = heappop(heap)
                if d != dist[i]:
                    continue
                for j, c in graph[i].items():
                    if d + c < dist[j]:
                        dist[j] = d + c
                        heappush(heap, (d + c, j))
            distances.append(dist)
        lengths = sorted(set(map(len, names)))
        n = len(source)
        dp = [10**30] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            for length in lengths:
                if i + length > n:
                    break
                a, b = source[i : i + length], target[i : i + length]
                if a in indices and b in indices:
                    dp[i + length] = min(
                        dp[i + length], dp[i] + distances[indices[a]][indices[b]]
                    )
        return dp[n] if dp[n] < 10**30 else -1
