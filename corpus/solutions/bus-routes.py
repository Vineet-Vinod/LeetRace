from typing import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        at = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                at[stop].append(i)
        queue = deque([(source, 0)])
        seen = {source}
        buses = set()
        while queue:
            stop, distance = queue.popleft()
            for bus in at[stop]:
                if bus in buses:
                    continue
                buses.add(bus)
                for nxt in routes[bus]:
                    if nxt == target:
                        return distance + 1
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, distance + 1))
        return -1
