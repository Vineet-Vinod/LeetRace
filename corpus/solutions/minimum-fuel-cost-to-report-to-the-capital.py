class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        size = len(roads) + 1
        graph: List[List[int]] = [[] for _ in range(size)]
        for first, second in roads:
            graph[first].append(second)
            graph[second].append(first)
        parent = [-1] * size
        order = [0]
        for city in order:
            for neighbor in graph[city]:
                if neighbor != parent[city]:
                    parent[neighbor] = city
                    order.append(neighbor)
        representatives = [1] * size
        fuel = 0
        for city in reversed(order[1:]):
            fuel += (representatives[city] + seats - 1) // seats
            representatives[parent[city]] += representatives[city]
        return fuel
