class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b, weight in edges:
            a -= 1
            b -= 1
            graph[a].append((b, weight))
            graph[b].append((a, weight))
        distance = [10**18] * n
        distance[-1] = 0
        heap = [(0, n - 1)]
        while heap:
            current_distance, node = heappop(heap)
            if current_distance != distance[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = current_distance + weight
                if candidate < distance[neighbor]:
                    distance[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))
        ways = [0] * n
        ways[-1] = 1
        for node in sorted(range(n), key=lambda x: distance[x]):
            for neighbor, _ in graph[node]:
                if distance[neighbor] > distance[node]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % (10**9 + 7)
        return ways[0]
