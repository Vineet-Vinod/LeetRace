class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> int:
        bike_count = len(bikes)
        costs = [10**9] * (1 << bike_count)
        costs[0] = 0
        for mask in range(1 << bike_count):
            worker = mask.bit_count()
            if worker >= len(workers):
                continue
            for bike, (bx, by) in enumerate(bikes):
                if not mask & (1 << bike):
                    wx, wy = workers[worker]
                    next_mask = mask | (1 << bike)
                    costs[next_mask] = min(
                        costs[next_mask], costs[mask] + abs(wx - bx) + abs(wy - by)
                    )
        return min(
            cost for mask, cost in enumerate(costs) if mask.bit_count() == len(workers)
        )
