from typing import List


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        best = [0] + [-(10**9)] * (n - 1)
        for week in range(len(days[0])):
            best = [
                max(
                    best[source]
                    for source in range(n)
                    if source == destination or flights[source][destination]
                )
                + days[destination][week]
                for destination in range(n)
            ]
        return max(best)
