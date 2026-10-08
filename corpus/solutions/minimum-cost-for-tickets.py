class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        travel_days = set(days)
        best = [0] * 366
        for day in range(1, 366):
            if day not in travel_days:
                best[day] = best[day - 1]
            else:
                best[day] = min(
                    best[max(0, day - 1)] + costs[0],
                    best[max(0, day - 7)] + costs[1],
                    best[max(0, day - 30)] + costs[2],
                )
        return best[365]
