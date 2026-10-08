class Solution:
    def minCost(
        self, n: int, roads: List[List[int]], appleCost: List[int], k: int
    ) -> List[int]:
        graph: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for first, second, cost in roads:
            first -= 1
            second -= 1
            weight = cost * (k + 1)
            graph[first].append((second, weight))
            graph[second].append((first, weight))
        distances = appleCost[:]
        heap = [(cost, city) for city, cost in enumerate(appleCost)]
        heapify(heap)
        while heap:
            cost, city = heappop(heap)
            if cost != distances[city]:
                continue
            for neighbor, weight in graph[city]:
                candidate = cost + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))
        return distances
