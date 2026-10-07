class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = [[] for _ in range(n)]
        for a, b, toll in highways:
            graph[a].append((b, toll))
            graph[b].append((a, toll))
        distance = [[inf] * (discounts + 1) for _ in range(n)]
        distance[0][0] = 0
        queue = [(0, 0, 0)]
        while queue:
            cost, city, used = heappop(queue)
            if cost != distance[city][used]:
                continue
            if city == n - 1:
                return cost
            for neighbor, toll in graph[city]:
                full_cost = cost + toll
                if full_cost < distance[neighbor][used]:
                    distance[neighbor][used] = full_cost
                    heappush(queue, (full_cost, neighbor, used))
                if used < discounts:
                    discounted = cost + toll // 2
                    if discounted < distance[neighbor][used + 1]:
                        distance[neighbor][used + 1] = discounted
                        heappush(queue, (discounted, neighbor, used + 1))
        return -1
